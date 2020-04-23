#! /usr/bin/env python
import os, requests, subprocess, argparse, logging, shutil
HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(HERE,'data')
URL = 'https://github.com/zhuowei/RaspberryJuice/raw/a2d49279de9396a56fbb3f10c477192d5b5ba28a/jars/raspberryjuice-1.12.1.jar'
PLUGINS = os.path.join(DATA,'plugins')
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
        '-b','--bedrock',
        default = False,
        action = 'store_true',
        help = 'If specified, start a Bedrock/Pocket edition proxy (DragonProxy)',
    )
    parser.add_argument(
        '-a','--authentication',
        default = False,
        action = 'store_true',
        help = 'If specified, authenticate against Minecraft.net servers (requires BedRock players to have their password handy)',
    )
    return parser

def install_raspberry_juice():
    """Install extension to allow for mcpi coding"""
    if not os.path.exists(PLUGINS):
        os.makedirs(PLUGINS)
    if not os.path.exists(JARFILE):
        log.info("Downloading RaspberryJuice plugin")
        response = requests.get(url)
        response.raise_for_status()
        with open(JARFILE,'wb') as fh:
            for chunk in response.iter_content(MEGA):
                fh.write(chunk)
def update_config():
    # target = target_ip()
    if not os.path.exists(DATA):
        os.makedirs(DATA)
    for filename in [
        'server.properties',
        'whitelist.json',
    ]:
        source,target = os.path.join(HERE,filename),os.path.join(DATA,filename)
        if os.path.exists(source):
            log.info("Copying %s to %s", source, target)
            shutil.copy(
                source,
                target,
            )

def main():
    parser = get_options()
    options = parser.parse_args()
    if not options.eula:
        parser.error('You have not accepted the EULA (-e) flag')
        return
    install_raspberry_juice()
    subprocess.call(['docker','stop',docker_name])
    subprocess.call(['docker','rm',docker_name])
    command = [
        'docker','run','-d','-p4711:4711','-p25565:25565',
        f'-v{HERE}/data:/data',
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
        if options.authentication:
            command.append('-a')
        subprocess.check_call(command)
    
if __name__ == "__main__":
    main()

