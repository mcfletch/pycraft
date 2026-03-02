"""Dashboard services container — holds Channel and SSEManager references"""


class DashboardServices:
    """Container for shared services accessible from all request handlers"""

    def __init__(self, channel, sse_manager):
        self.channel = channel
        self.sse_manager = sse_manager
        self.connected = False
