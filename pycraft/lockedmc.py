"""Utility to run mc operations with a threading.RLock"""
import contextlib
import threading
import functools
LOCK_KEY = '__threadlock'

@contextlib.contextmanager
def locked(mc):
    if mc:
        current = mc.__dict__.get(LOCK_KEY)
        if current is None:
            current = mc.__dict__.setdefault(LOCK_KEY,threading.RLock())
        current.acquire(True)
        yield current 
        current.release()
    else:
        yield mc

def with_lock_held(function):
    """Decorate a method to acquire the `self.mc` lock"""
    @functools.wraps(function)
    def lock_held(self,*args,**named):
        mc = self.__dict__.get('mc')
        with locked(mc):
            return function(self,*args,**named)
    return lock_held