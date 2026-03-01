"""Shared pytest fixtures for pycraft tests.

The ``live`` marker is used for tests that require a running Minecraft
server with the PycraftServer plugin listening on localhost:4712.

Run only live tests::

    pytest -m live

Skip live tests::

    pytest -m "not live"
"""

import asyncio
import socket
import subprocess
import time

import pytest
import pytest_asyncio

from pycraft.server.channel import Channel


def _server_is_reachable(host='localhost', port=4712, timeout=2):
    """Return True if we can open a TCP connection to the PycraftServer port."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _wait_for_server(host='localhost', port=4712, retries=60, interval=5):
    """Block until the PycraftServer TCP port is accepting connections."""
    for _ in range(retries):
        if _server_is_reachable(host, port):
            return True
        time.sleep(interval)
    return False


@pytest.fixture(scope='session')
def live_server():
    """Ensure a Minecraft server with PycraftServer is running.

    If a server is already listening on port 4712 it is reused.
    Otherwise ``run.py`` is invoked to start one and the fixture
    waits until PycraftServer is ready before yielding.
    """
    if _server_is_reachable():
        yield 'localhost'
        return

    proc = subprocess.Popen(
        [
            'python3',
            'run.py',
            '-e',
            '-d',
            'worlds/test/',
            '--no-chat',
            '--version',
            '1.21.11',
        ],
        cwd='/home/mcfletch/pycraft',
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    try:
        if not _wait_for_server():
            raise RuntimeError(
                'Minecraft server did not become reachable on port 4712'
            )
        yield 'localhost'
    finally:
        proc.terminate()
        proc.wait(timeout=30)


@pytest_asyncio.fixture(scope='session', loop_scope='session')
async def channel(live_server):
    """Session-scoped Channel connected to the live server.

    Introspection metadata is loaded once and shared across all tests
    that use this fixture, avoiding the overhead of re-fetching the
    large metadata payload for every test case.
    """
    chan = Channel(host=live_server, port=4712, debug=False)
    await chan.open()
    await chan.introspect(cached=True)
    yield chan
    await chan.close()
