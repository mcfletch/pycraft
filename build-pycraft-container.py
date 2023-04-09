#! /usr/bin/env python3
import subprocess, logging, os, shutil, sys
RELEASE_PREFIX = 'release-'
DOCKER_TAG_TEMPLATE = 'mcfletch/pycraft-chat-server:%(tag)s'
log = logging.getLogger('build')

def get_releases():
    tags = [
        tag for tag in 
        subprocess.check_output(['git','describe','--abbrev=0','--tags']).decode('utf-8').splitlines()
        if tag.startswith(RELEASE_PREFIX)
    ]
    releases = []
    for tag in tags:
        release = [int(x) for x in tag[len(RELEASE_PREFIX):].split('.')]
        releases.append((tuple(release),tag))
    releases.sort()
    return releases

def get_options():
    import argparse
    parser = argparse.ArgumentParser(description='Build (and optionally tag and push) container')
    parser.add_argument('-p','--push',action='store_true',default=False,help='If true, push the resulting container to docker hub, increment version and record new tag')
    return parser

def build(release):
    version,tag = release
    new_version = (version[0],version[1],version[2]+1)
    docker_tag = '%d.%d.%d'%new_version
    subprocess.check_call([
        'docker','build',
            '--tag',DOCKER_TAG_TEMPLATE%{'tag':docker_tag},
            '--tag',DOCKER_TAG_TEMPLATE%{'tag':'latest'},
            '.',
    ])
    return new_version

INCLUDE_FILES = [
    'server.properties',
    'whitelist.json',
    'Geyser-config.yml',
    'README.md',
    'plugins/PycraftServer-1.0.6.jar',
]

def pack_runner(release):
    """Create the small runner program that runs the various bits"""
    includes = []
    for filename in INCLUDE_FILES :
        if os.path.exists(filename):
            includes.extend(['--add-data','%s:%s'%(filename,filename)])
    dist_target = os.path.abspath('dist/pycraft-runner')
    if os.path.exists(dist_target):
        shutil.rmtree(dist_target)
    subprocess.check_call([
        'pyinstaller',
            '--clean',
    ]+includes+[
        '-n','pycraft-runner',
        '--console',
        'run.py',
    ])
    output_file = os.path.abspath(f'dist/pycraft-runner-{sys.platform}-{release[0]}.{release[1]}.{release[2]}.zip')
    print('Zipping to', output_file)
    subprocess.check_call([
        'zip',
        '-9',
        '-r',
        output_file,
    ]+os.listdir(dist_target),cwd=dist_target)

def main():
    options = get_options().parse_args()
    releases = get_releases()
    assert releases, """No tags of the form release-%d.%d.%d in git"""
    new_version = build(releases[-1])
    log.info("Built release %d.%d.%d", new_version[0],new_version[1],new_version[2])
    pack_runner(new_version)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
