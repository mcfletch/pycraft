#! /usr/bin/env python
import os, requests, subprocess, yaml, argparse, logging
HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(HERE,'data')
JARFILE = os.path.join(DATA,'DragonProxy.jar')
log = logging.getLogger('dragon-proxy-setup')

url = 'https://ci.codemc.io/job/DragonetMC/job/DragonProxy/lastSuccessfulBuild/artifact/bootstrap/standalone/target/DragonProxy.jar'
docker_name = 'mc-dragon-proxy'
MEGA = 1024*1024
def acquire_jar():
    if not os.path.exists(DATA):
        os.makedirs(DATA)
    if not os.path.exists(JARFILE):
        log.info("Downloading DragonProxy")
        response = requests.get(url)
        response.raise_for_status()
        with open(JARFILE,'wb') as fh:
            for chunk in response.iter_content(MEGA):
                fh.write(chunk)

def get_options():
    parser = argparse.ArgumentParser(
        description='Run a dragon proxy service for BedRock clients in docker',
    )
    parser.add_argument(
        '-t','--target',
        default = 'minecraft',
        help = 'Specify the ip address or host-name of the minecraft server',
    )
    parser.add_argument(
        '-a','--authentication',
        default = False,
        action = 'store_true',
        help = 'If specified, authenticate against Minecraft.net servers (requires BedRock players to have their password handy)',
    )
    return parser

def guess_target(target):
    if not target:
        log.info("No listen specified, looking up route to the internet")
        try:
            target = subprocess.check_output([
                'ip','route','get','8.8.8.8',
            ]).decode('latin-1').split()[2]
        except Exception as err:
            parser.error(
                'Unable to determine the default ipv4 route to the internet'
            )
            raise
        else:
            log.info('  Using %s as listen',target)
    return target


def update_config(target=None,auth=False):
    target = guess_target(target)
    conf = yaml.safe_load(open(os.path.join(HERE,'config.yml')))
    conf['remote-address'] = target
    conf['remote-auth'] = 'credentials' if auth else 'offline'
    with open(os.path.join(DATA,'config.yml'),'w') as fh:
        yaml.safe_dump(conf,fh)
    return conf

def start_docker():
    options = get_options().parse_args()
    acquire_jar()
    conf = update_config()
    container_name = 'mc-dragon-proxy'
    subprocess.call(['docker','stop',docker_name])
    subprocess.call(['docker','rm',docker_name])
    command = [
        'docker','run','-d','-ephemeral',
        '--name',docker_name,
        "-p19132:19132/udp",
        '-v',f'{DATA}:/code',
        '--workdir','/code',
        'adoptopenjdk/maven-openjdk8:latest',
        '/opt/java/openjdk/bin/java','-jar','/code/DragonProxy.jar',
    ]
    subprocess.check_call(command)
    log.info(
        "BedRock proxy running on port: %s => %s",
        19132,
        conf['remote-address'],
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_docker()
