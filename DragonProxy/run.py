#! /usr/bin/env python
import os, requests, subprocess, yaml
HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.join(HERE,'data')
JARFILE = os.path.join(DATA,'DragonProxy.jar')

url = 'https://ci.codemc.io/job/DragonetMC/job/DragonProxy/lastSuccessfulBuild/artifact/bootstrap/standalone/target/DragonProxy.jar'
docker_name = 'mc-dragon-proxy'
MEGA = 1024*1024
def acquire_jar():
    if not os.path.exists(DATA):
        os.makedirs(DATA)
    if not os.path.exists(JARFILE):
        response = requests.get(url)
        response.raise_for_status()
        with open(JARFILE,'wb') as fh:
            for chunk in response.iter_content(MEGA):
                fh.write(chunk)
def target_ip(name='minecraft'):
    return subprocess.check_output([
        'docker','inspect','--format','{{ .NetworkSettings.IPAddress }}',
        name,
    ]).strip()
def update_config():
    target = target_ip()
    conf = yaml.safe_load(open(os.path.join(HERE,'config.yml')))
    conf['remote-address'] = target
    with open(os.path.join(DATA,'config.yml'),'w') as fh:
        yaml.safe_dump(conf,fh)

def start_docker():
    acquire_jar()
    update_config()
    subprocess.call(['docker','stop','mc-dragon-proxy'])
    subprocess.call(['docker','rm','mc-dragon-proxy'])
    command = [
        'docker','run','-d','-ephemeral',
        '--name',docker_name,
        '-v',f'{DATA}:/code',
        '--workdir','/code',
        'adoptopenjdk/maven-openjdk8:latest',
        '/opt/java/openjdk/bin/java','-jar','/code/DragonProxy.jar',
    ]
    subprocess.check_call(command)

if __name__ == "__main__":
    start_docker()