"""Hot reload functionality"""
import os, sys, logging, subprocess, time
HERE = os.path.abspath(os.path.dirname(__file__))
log = logging.getLogger(__name__)
def hot_reload(watchdirs=None,extensions='*.py',callback=None):
    """Restart the server every time a (python) file is changed"""
    watchdirs = watchdirs or [HERE]
    log.info("Watching for changes to files in %s", watchdirs)
    events = []
    for e_name in [
        'close_write',
        'moved_to',
        'moved_from',
        'move',
        'delete',
    ]:
        events.extend([
            '-e',e_name,
        ])
    pipe = subprocess.Popen([
        'inotifywait',
        '-r',
    ] + events + [
        '--exclude=".*[.]pyc"',
    ] + watchdirs)
    while pipe.poll() is None:
        time.sleep(2)
    # pipe.wait()
    log.warning("Change detected, reloading")
    if callback:
        callback()
    os.execv(sys.argv[0],sys.argv,)
