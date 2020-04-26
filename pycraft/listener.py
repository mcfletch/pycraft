"""Expose commands via chat on a minecraft instance"""
from mcpi import minecraft, block, connection
from mcpi.vec3 import Vec3
import threading, logging, inspect, operator
import re, time, ast
import contextlib, functools
from .expose import (
    DEFAULT_COMMANDS,
    DEFAULT_NAMESPACE,
    expose,
)
import queue
from .lockedmc import locked
from . import entity
import numpy as np
log = logging.getLogger(__name__)
COMMAND_FINDER = re.compile(
    r'^[ ]*(?P<function>[a-zA-z][_.a-zA-Z0-9]*)[(](?P<args>.*)[)][ ]*$',
    re.I|re.U
)
ASSIGNMENT_FINDER = re.compile(
    r'^[ ]*(?P<name>[a-zA-z][_a-zA-Z0-9]*)[ ]*[=](?P<expr>.*)[ ]*$',
    re.I|re.U,
)


class Listener(object):
    wanted = True
    def __init__(self, mc, interpreter=None):
        self.mc = mc 
        self.request_queue = queue.Queue()
        self.response_queue = queue.Queue()
        if interpreter is None:
            from . import interpreter as default_interpreter
            interpreter = default_interpreter.Interpreter(
                self.mc,
            )
        self.commands = interpreter
    
    def poll(self):
        """Poll for chat messages and see if we recognise them"""
        empty_count = 0
        while self.wanted:
            with locked(self.mc):
                try:
                    messages = self.mc.events.pollChatPosts()
                except connection.RequestError as err:
                    log.warning("Error on poll chat: %s", err)
                    messages = []
                except ValueError as err:
                    log.exception("Unhandled error in mcpi, ignoring")
                    messages = []
            for message in messages:
                match = COMMAND_FINDER.match(message.message)
                if match:
                    log.debug("Request: %s", message)
                    self.request_queue.put(message)
                else:
                    match = ASSIGNMENT_FINDER.match(message.message)
                    if match:
                        message.assignment = match.group('name')
                        message.message = match.group('expr').strip()
                        self.request_queue.put(message)
            if not messages:
                empty_count += 1
            else:
                empty_count = 0
            if empty_count:
                delay = min((.1*empty_count,2))
                log.debug("Sleep for %ss",delay)
                time.sleep(delay)
    def responder(self):
        """Thread that returns responses to requests via Chat"""
        while self.wanted:
            try:
                response = self.response_queue.get(True,5)
            except queue.Empty:
                continue
            with locked(self.mc):
                for line in response.chat_messages():
                    self.mc.postToChat(line)
    def interpreter(self):
        while self.wanted:
            try:
                request = self.request_queue.get(True,5)
            except queue.Empty:
                continue
            try:
                response = self.commands.interpret(request)
            except Exception as err:
                log.exception(
                    'Error handling %r',
                    request,
                )
            else:
                if response:
                    self.response_queue.put(response)


