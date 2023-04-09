#! /usr/bin/env python3
import os, requests, subprocess, argparse, logging, shutil, yaml, glob

HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(HERE, 'data')
GEYSER_URL = 'https://ci.opencollab.dev//job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/artifact/bootstrap/spigot/target/Geyser-Spigot.jar'
PYCRAFT_SERVER_URL = 'https://github.com/mcfletch/pycraft-server/releases/download/v-1.0.6/PycraftServer-1.0.6.jar'
PLUGINS = 'plugins'
PLUGIN_SOURCE = os.path.join(HERE, PLUGINS)
# JARFILE = URL.split('/')[-1]
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
        help='If specified, authenticate against Minecraft.net servers (requires BedRock players to have their Java Edition password handy)',
    )
    parser.add_argument(
        '--wipe-config',
        default=False,
        action='store_true',
        help='If specified overwrite the data-directory\'s server.properties and whitelist.json with those in this directory',
    )
    parser.add_argument(
        '--no-chat',
        default=True,
        dest='chat',
        action='store_false',
        help='Do not start the pycraft-chat-server container (used during development to allow for running it from the source-code tree)',
    )
    parser.add_argument(
        '--stop',
        default=False,
        dest='stop',
        action='store_true',
        help='If specified, shut down the containers using docker stop',
    )
    return parser


def install_pycraftserver_plugin(data, bedrock=True):
    """Install extension to allow for mcpi coding

    If bedrock is True, then *also* install the geyser
    bedrock edition bridge.
    """
    plugins = os.path.join(data, PLUGINS)
    if not os.path.exists(plugins):
        os.makedirs(plugins)
    log.info("World plugin dir: %s", plugins)
    for filename in glob.glob(os.path.join(plugins, 'PycraftServer-*.jar')):
        os.remove(filename)

    for url in [
        x
        for x in [
            PYCRAFT_SERVER_URL,
            GEYSER_URL if bedrock else None,
        ]
        if x
    ]:
        base = url.split('/')[-1]
        cache = os.path.join(PLUGIN_SOURCE, base)
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
        else:
            log.info('  %s already there', jarfile)
        shutil.copy(cache, jarfile)


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
    chat_name = docker_name + '-chatserver'
    if options.stop:
        for name in [docker_name,chat_name]:
            subprocess.call(['docker','stop',name]) # note: we do *not* check results here...
        subprocess.call(['docker','ps'])
        return
    if not options.eula:
        parser.error('You have not indicated that you have accepted the Minecraft Server EULA (read and add the -e) flag')
        return
    data = os.path.normpath(os.path.abspath(options.data))
    install_pycraftserver_plugin(data, options.bedrock)
    if options.bedrock:
        configure_geyser(data, options.authentication)
    update_config(data, overwrite=options.wipe_config)
    subprocess.call(['docker', 'stop', docker_name])
    subprocess.call(['docker', 'rm', docker_name])
    subprocess.check_call(['docker', 'pull', 'itzg/minecraft-server'])
    command = [
        'docker',
        'run',
        '--rm',
        '-d',
        '-p4712:4712',
        '-p25565:25565',
        "-p19132:19132/udp",
        f'-v{data}:/data',
        '-e',
        # 'TYPE=SPIGOT',
        'TYPE=PUFFERFISH',
        # 'TYPE=PAPER',
        '-eMEMORY=2g',
        '-eEULA=TRUE',
        '--name',
        docker_name,
        'itzg/minecraft-server:java19',
    ]
    subprocess.check_output(command)
    log.info("Java Edition server on port: %s", 25565)
    if options.bedrock:
        log.info("Bedrock Edition server on port: %s", 19132)
    if options.chat:
        server_ip = subprocess.check_output([
            'docker','inspect','-f','{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}',
            docker_name,
        ]).decode('utf-8').strip()
        log.info("Server container is on ip: %s", server_ip)

        if server_ip:
            subprocess.check_call([
                'docker',
                'run',
                '--rm',
                '-d',
                '--name',chat_name,
                'mcfletch/pycraft-chat-server:latest',
                '-H', server_ip,
            ])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
