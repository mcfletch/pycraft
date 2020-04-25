#! /usr/bin/env python
import os, requests, subprocess, argparse, logging, shutil
HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(HERE,'data')
URL = 'https://github.com/zhuowei/RaspberryJuice/raw/a2d49279de9396a56fbb3f10c477192d5b5ba28a/jars/raspberryjuice-1.12.1.jar'
PLUGINS = os.path.join('plugins')
JARFILE = os.path.join(PLUGINS,'raspberryjuice-1.12.1.jar')
log = logging.getLogger('pycraft-setup')
docker_name = 'minecraft'
MEGA = 1024*1024

def get_options():
    parser = argparse.ArgumentParser(
        description='Run a RaspberryJuice enhanced Bukkit server inside docker'
    )
    parser.add_argument(
        '-e','--eula',
        default = False,
        action = 'store_true',
        help = 'You must specify this argument to indicate that you have read the EULA',
    )
    parser.add_argument(
        '-d','--data',
        default=DATA,
        help='Override the default server to run (e.g. to use a scratch server/dataset)',
    )
    parser.add_argument(
        '-n','--name',
        default=docker_name,
        help='Override the default docker name',
    )
    parser.add_argument(
        '-b','--bedrock',
        default = False,
        action = 'store_true',
        help = 'If specified, start a Bedrock/Pocket edition proxy (DragonProxy/run.py)',
    )
    parser.add_argument(
        '-l','--listen',
        default = None,
        help='Specify the ip address to advertise to the BedRock proxy server (if we are starting it)',
    )
    parser.add_argument(
        '-a','--authentication',
        default = False,
        action = 'store_true',
        help = 'If specified, authenticate against Minecraft.net servers (requires BedRock players to have their password handy)',
    )
    return parser

def install_raspberry_juice(data):
    """Install extension to allow for mcpi coding"""
    plugins = os.path.join(data,PLUGINS)
    if not os.path.exists(plugins):
        os.makedirs(plugins)
    jarfile = os.path.join(data,JARFILE)
    cache = os.path.join(HERE, os.path.basename(JARFILE))
    if not os.path.exists(cache):
        log.info("Downloading RaspberryJuice plugin")
        response = requests.get(URL)
        response.raise_for_status()
        with open(cache,'wb') as fh:
            for chunk in response.iter_content(MEGA):
                fh.write(chunk)
    if not os.path.exists(jarfile):
        shutil.copy(cache,jarfile)
def update_config(data):
    # target = target_ip()
    if not os.path.exists(data):
        os.makedirs(data)
    for filename in [
        'server.properties',
        'whitelist.json',
    ]:
        source,target = os.path.join(HERE,filename),os.path.join(data,filename)
        if os.path.exists(source):
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
    target = options.listen
    data = os.path.abspath(options.data)
    install_raspberry_juice(data)
    update_config(data)
    subprocess.call(['docker','stop',docker_name])
    subprocess.call(['docker','rm',docker_name])
    subprocess.check_call(['docker','pull','itzg/minecraft-server'])
    command = [
        'docker','run','-d','-p4711:4711','-p25565:25565',
        f'-v{data}:/data',
        '-e','TYPE=BUKKIT',
        '-eEULA=TRUE',
        '--name',docker_name,
        'itzg/minecraft-server',
    ]
    subprocess.check_output(command)
    log.info("Java Edition server on port: %s", 25565)
    if options.bedrock:
        log.info("Starting DragonProxy plugin installation")
        command = [
            'python',
            os.path.join('DragonProxy','run.py'),
        ]
        if target:
            options.extend(['-t',target])
        if options.authentication:
            command.append('-a')
        subprocess.check_call(command)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

