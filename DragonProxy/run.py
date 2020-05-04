#! /usr/bin/env python3
import os, requests, subprocess, yaml, argparse, logging
import shutil, tempfile, time
HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(HERE,'data')
JARFILE = os.path.join(HERE,'DragonProxy.jar')
log = logging.getLogger('dragon-proxy-setup')

url = 'https://ci.codemc.io/job/DragonetMC/job/DragonProxy/lastSuccessfulBuild/artifact/bootstrap/standalone/target/DragonProxy.jar'
docker_name = 'mc-dragon-proxy'
MEGA = 1024*1024
def acquire_jar(data=DATA):
    if not os.path.exists(data):
        os.makedirs(data)
    if not os.path.exists(JARFILE):
        log.info("Downloading DragonProxy")
        response = requests.get(url)
        response.raise_for_status()
        with open(JARFILE,'wb') as fh:
            for chunk in response.iter_content(MEGA):
                fh.write(chunk)
    else:
        log.info("Using cached DragonProxy")
    final = os.path.join(data,os.path.basename(JARFILE))
    if not os.path.exists(final):
        log.info("Installing DragonProxy")
        shutil.copy(JARFILE,final)

def get_options():
    parser = argparse.ArgumentParser(
        description='Run a DragonProxy service for BedRock clients in docker',
    )
    parser.add_argument(
        '-t','--target',
        default = None,
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

def generate_default_config():
    temp = tempfile.mkdtemp(prefix='dragon-proxy-')
    try:
        acquire_jar(temp)
        command = [
            'docker','run','-i','-a','STDIN',
        ] + common_args(temp)
        command = "echo 'stop' | %s"%(
            " ".join(command)
        )
        # print('Final command to generate config: %s'%(command,))
        pipe = subprocess.Popen(
            command,
            shell=True
        )
        pipe.wait()
        expected = os.path.join(temp,'config.yml')
        for i in range(30):
            if not os.path.exists(expected):
                time.sleep(0.1)
            else:
                break
        conf = yaml.safe_load(open(expected))
        return conf
    finally:
        shutil.rmtree(temp)


def update_config(target=None,auth=False):
    current_default = generate_default_config()
    target = guess_target(target)
    conf = generate_default_config()
    conf['remote-address'] = target
    conf['remote-auth'] = 'credentials' if auth else 'offline'
    conf['max-players'] = 20
    with open(os.path.join(DATA,'config.yml'),'w') as fh:
        yaml.safe_dump(conf,fh)
    return conf

def common_args(data=DATA):
    return [
        '-v',f'{data}:/code',
        '--workdir','/code',
        '--user','%s:%s'%(os.getuid(),os.getgid()),
        'adoptopenjdk/maven-openjdk8:latest',
        '/opt/java/openjdk/bin/java','-jar','/code/DragonProxy.jar',
    ]
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
    ] + common_args()

    print(' '.join(command))
    subprocess.check_call(command)
    log.info(
        "BedRock proxy running on port: %s => %s",
        19132,
        conf['remote-address'],
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_docker()
