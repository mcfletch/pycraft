"""Expose commands via chat on a minecraft instance"""
from mcpi import minecraft, block, connection
from mcpi.vec3 import Vec3
import asyncio
import logging
import re, time
from .expose import (
    DEFAULT_COMMANDS,
    DEFAULT_NAMESPACE,
    expose,
)
import queue

# from .lockedmc import locked
from . import entity
import numpy as np

log = logging.getLogger(__name__)
COMMAND_FINDER = re.compile(
    r'^[ ]*(?P<function>[a-zA-z][_.a-zA-Z0-9]*)[(](?P<args>.*)[)][ ]*$', re.I | re.U
)
ASSIGNMENT_FINDER = re.compile(
    r'^[ ]*(?P<name>[a-zA-z][_a-zA-Z0-9]*)[ ]*[=](?P<expr>.*)[ ]*$',
    re.I | re.U,
)


class AListener(object):
    """Asyncio compatible listening service"""

    wanted = True

    def __init__(self, channel, interpreter=None):
        self.channel = channel
        if interpreter is None:
            from . import ainterpreter as default_interpreter

            interpreter = default_interpreter.AInterpreter(channel)
        self.interpreter = interpreter

    async def listen(self):
        """Arrang to run our chat processing operations in the background"""
        self.request_queue = await self.channel.subscribe("AsyncPlayerChatEvent")
        asyncio.ensure_future(self.process_chat_queue(self.request_queue))

    async def process_chat_queue(self, queue):
        """Process chat events from the queue"""
        try:
            while self.wanted:
                log.info("Getting message...")
                message = await queue.get()
                log.debug("Message: %s", message)
                match = COMMAND_FINDER.match(message.message)
                if match:
                    asyncio.ensure_future(self.process_command(message))
                else:
                    match = ASSIGNMENT_FINDER.match(message.message)
                    if match:
                        message.assignment = match.group('name')
                        message.message = match.group('expr').strip()
                        asyncio.ensure_future(self.process_command(message))
            log.info("Wanted False, exiting process chat queue")
        except Exception as err:
            log.exception("Failure during process chat queue, will restart")
            asyncio.ensure_future(self.process_chat_queue(queue))

    async def process_command(self, message):
        """Process a command that does not make an assignment"""
        response = await self.interpreter.interpret(message)
        if response is not None:
            await self.channel.server.broadcastMessage(str(response))
