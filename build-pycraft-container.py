#! /usr/bin/env python3
import subprocess, logging, os, shutil, sys

RELEASE_PREFIX = 'release-'
DOCKER_TAG_TEMPLATE = 'mcfletch/pycraft-chat-server:%(tag)s'
log = logging.getLogger('build')


def get_releases():
    tags = []
    for tag in (
        subprocess.check_output(['git', 'describe', '--abbrev=0', '--tag'])
        .decode('utf-8')
        .splitlines()
    ):
        tag = tag.strip()
        log.info('tag: %s', tag)
        if tag.strip().startswith(RELEASE_PREFIX):
            tags.append(tag)
    releases = []
    for tag in tags:
        release = [int(x) for x in tag[len(RELEASE_PREFIX) :].split('.')]
        releases.append((tuple(release), tag))
    releases.sort()
    return releases


def get_options():
    import argparse

    parser = argparse.ArgumentParser(
        description='Build (and optionally tag and push) container'
    )
    parser.add_argument(
        '-r',
        '--runner',
        action='store_true',
        default=False,
        help='If true, only build the runner for current release and exit',
    )
    parser.add_argument(
        '-p',
        '--push',
        action='store_true',
        default=False,
        help='If true, push the resulting container to docker hub, increment version and record new tag',
    )
    return parser


def build(release):
    version, tag = release
    new_version = (version[0], version[1], version[2] + 1)
    docker_tag = '%d.%d.%d' % new_version
    tags = [
        DOCKER_TAG_TEMPLATE % {'tag': docker_tag},
        DOCKER_TAG_TEMPLATE % {'tag': 'latest'},
    ]
    tagset = []
    for tag in tags:
        tagset.extend(['--tag', tag])
    subprocess.check_call(
        [
            'docker',
            'build',
        ]
        + tagset
        + [
            '.',
        ]
    )
    return new_version, tags


INCLUDE_FILES = [
    'server.properties',
    'whitelist.json',
    'Geyser-config.yml',
    'README.md',
    'plugins/PycraftServer-1.0.7.jar',
]


def pack_runner(release):
    """Create the small runner program that runs the various bits"""
    includes = []
    for filename in INCLUDE_FILES:
        if os.path.exists(filename):
            includes.extend(
                [
                    '--add-data',
                    '%s%s%s' % (filename, os.pathsep, os.path.dirname(filename) or '.'),
                ]
            )
    dist_target = os.path.abspath('dist/pycraft-runner')
    if os.path.exists(dist_target):
        shutil.rmtree(dist_target)
    command = (
        [
            'pyinstaller',
            '--clean',
        ]
        + includes
        + [
            '-n',
            'pycraft-runner',
            '--console',
            'run.py',
        ]
    )
    log.info("Pyinstaller: %s", " ".join(command))
    subprocess.check_call(command)
    output_file = os.path.abspath(
        f'dist/pycraft-runner-{sys.platform}-{release[0]}.{release[1]}.{release[2]}.zip'
    )
    print('Zipping to', output_file)
    if os.path.exists(output_file):
        os.remove(output_file)
    subprocess.check_call(
        [
            'zip',
            '-9',
            '-r',
            output_file,
        ]
        + os.listdir(dist_target),
        cwd=dist_target,
    )


def main():
    options = get_options().parse_args()
    releases = get_releases()
    assert releases, """No annotated tags of the form release-%d.%d.%d in git"""
    if options.runner:
        log.info("Rebuilding runner")
        pack_runner(releases[-1][0])
        return
    else:
        new_version, tags = build(releases[-1])
        log.info(
            "Built release %d.%d.%d", new_version[0], new_version[1], new_version[2]
        )
        pack_runner(new_version)

    if options.push:
        for tag in tags:
            subprocess.check_call(['docker', 'push', tag])
        subprocess.check_call(
            [
                'git',
                'tag',
                '-a',
                '-m',
                "Release %s.%s.%s" % new_version,
                '%s%d.%d.%d'
                % (RELEASE_PREFIX, new_version[0], new_version[1], new_version[2]),
            ]
        )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
