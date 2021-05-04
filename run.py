#! /usr/bin/env python3
import os, requests, subprocess, argparse, logging, shutil, yaml

HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(HERE, 'data')
URL = 'https://github.com/zhuowei/RaspberryJuice/raw/a2d49279de9396a56fbb3f10c477192d5b5ba28a/jars/raspberryjuice-1.12.1.jar'
GEYSER_URL = 'https://ci.opencollab.dev//job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/artifact/bootstrap/spigot/target/Geyser-Spigot.jar'
PLUGINS = 'plugins'
JARFILE = URL.split('/')[-1]
GEYSER_JARFILE = GEYSER_URL.split('/')[-1]
log = logging.getLogger('pycraft-setup')
docker_name = 'minecraft'
MEGA = 1024 * 1024
GEYSER_CONFIG = 'Geyser-config.yml'


def get_options():
    parser = argparse.ArgumentParser(
        description='Run a RaspberryJuice enhanced Spigot (Bukkit) server inside docker'
    )
    parser.add_argument(
        '-e',
        '--eula',
        default=False,
        action='store_true',
        help='You must specify this argument to indicate that you have read the EULA',
    )
    parser.add_argument(
        '-d',
        '--data',
        default=DATA,
        help='Override the default server to run (e.g. to use a scratch server/dataset)',
    )
    parser.add_argument(
        '-n',
        '--name',
        default=docker_name,
        help='Override the default docker name',
    )
    parser.add_argument(
        '-b',
        '--bedrock',
        default=True,
        action='store_true',
        help='If specified, install the Geyser plugin in the world (default)',
    )
    parser.add_argument(
        '--no-bedrock',
        default=False,
        dest='bedrock',
        action='store_false',
        help='If specified, do not install the Geyser plugin in the world',
    )
    parser.add_argument(
        '-a',
        '--authentication',
        default=False,
        action='store_true',
        help='If specified, authenticate against Minecraft.net servers (requires BedRock players to have their password handy)',
    )
    parser.add_argument(
        '--wipe-config',
        default=False,
        action='store_true',
        help='If specified overwrite the data-directory\'s server.properties and whitelist.json with those in this directory',
    )
    return parser


def install_raspberry_juice(data, bedrock=True):
    """Install extension to allow for mcpi coding

    If bedrock is True, then *also* install the geyser
    bedrock edition bridge.
    """
    plugins = os.path.join(data, PLUGINS)
    if not os.path.exists(plugins):
        os.makedirs(plugins)
    log.info("World plugin dir: %s", plugins)

    for url in [
        x
        for x in [
            URL,
            GEYSER_URL if bedrock else None,
        ]
        if x
    ]:
        base = url.split('/')[-1]
        cache = os.path.join(HERE, base)
        jarfile = os.path.join(plugins, base)
        if not os.path.exists(cache):
            log.info("Downloading %s plugin", base)
            response = requests.get(url)
            response.raise_for_status()
            with open(cache, 'wb') as fh:
                for chunk in response.iter_content(MEGA):
                    fh.write(chunk)
        log.info("Copying %s to plugins", base)
        if not os.path.exists(jarfile):
            log.info(" %s => %s", base, jarfile)
            shutil.copy(cache, jarfile)
        else:
            log.info('  %s already there', jarfile)


def configure_geyser(data, auth=False):
    """Configure geyser with the config in this directory"""
    config_dir = os.path.join(data, 'plugins', 'Geyser-Spigot')
    target_config = os.path.join(config_dir, 'config.yml')
    if os.path.exists(target_config):
        content = yaml.safe_load(open(target_config))
    elif os.path.exists(GEYSER_CONFIG):
        content = yaml.safe_load(open(GEYSER_CONFIG))
    else:
        log.warning(
            "No current Geyser-config.yml (in this directory) or plugins/Geyser-Spigot/config.yml found, not configuring"
        )
        return
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    if auth:
        log.warning(
            'Setting up geyser in authenticating mode, which means the user will need a *java-edition* login to connect'
        )
        content['remote']['auth-type'] = 'online'
    else:
        content['remote']['auth-type'] = 'offline'
    log.info("Writing Geyser configuration in: %s", target_config)
    yaml.dump(content, open(target_config + '~', 'w'))
    os.rename(target_config + '~', target_config)


def update_config(data, overwrite=True):
    # target = target_ip()
    if not os.path.exists(data):
        os.makedirs(data)
    for filename in [
        'server.properties',
        'whitelist.json',
    ]:
        source, target = os.path.join(HERE, filename), os.path.join(data, filename)
        if os.path.exists(source):
            if overwrite or not os.path.exists(target):
                log.info("Copying %s to %s", source, target)
                shutil.copy(
                    source,
                    target,
                )


def main():
    parser = get_options()
    options = parser.parse_args()
    docker_name = options.name
    if not options.eula:
        parser.error('You have not accepted the EULA (read and add the -e) flag')
        return
    data = os.path.abspath(options.data)
    install_raspberry_juice(data, options.bedrock)
    if options.bedrock:
        configure_geyser(data, options.authentication)
    update_config(data, overwrite=options.wipe_config)
    subprocess.call(['docker', 'stop', docker_name])
    subprocess.call(['docker', 'rm', docker_name])
    subprocess.check_call(['docker', 'pull', 'itzg/minecraft-server'])
    command = [
        'docker',
        'run',
        '-d',
        '-p4711:4711',
        '-p4712:4712',
        '-p25565:25565',
        "-p19132:19132/udp",
        f'-v{data}:/data',
        '-e',
        'TYPE=SPIGOT',
        '-eEULA=TRUE',
        '--name',
        docker_name,
        'itzg/minecraft-server',
    ]
    subprocess.check_output(command)
    log.info("Java Edition server on port: %s", 25565)
    if options.bedrock:
        log.info("Java Edition server on port: %s", 19132)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
