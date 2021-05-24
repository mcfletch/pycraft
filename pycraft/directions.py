"""Utility functions for directions and locations"""
import numpy as np
from .server.world import Vector


def roughly_forward(direction):
    """Given a direction, figure out cartesian forward"""
    dx, dy, dz = direction[:3]
    if dx and dz:
        adx = np.abs(dx)
        adz = np.abs(dz)
        if adx > adz:
            if dx > 0:
                forward = Vector(1, 0, 0)
            else:
                forward = Vector(-1, 0, 0)
        else:
            if dz > 0:
                forward = Vector(0, 0, 1)
            else:
                forward = Vector(0, 0, -1)
    elif dx:
        if dx < 0:
            return Vector(-1, 0, 0)
        else:
            return Vector(1, 0, 0)
    elif dz:
        if dz < 0:
            return Vector(0, 0, -1)
        else:
            return Vector(0, 0, 1)
        return direction
    else:
        if dy > 0:
            forward = Vector(0, 1, 0)
        else:
            forward = Vector(0, -1, 0)
    return forward


def as_cube(start, stop):
    """Get start and size as a positive-step cube (so each coordinate is increasing)

    Returns two vectors (start, size) (regardless of the incoming types)
    """
    sx, sy, sz = start[:3]
    ex, ey, ez = stop[:3]
    return (
        Vector(
            min(sx, ex),
            min(sy, ey),
            min(sz, ez),
        ),
        # the +1 is to handle open-interval on the iteration on the server
        Vector(
            max(sx, ex) - min(sx, ex) + 1,
            max(sy, ey) - min(sy, ey) + 1,
            max(sz, ez) - min(sz, ez) + 1,
        ),
    )


def forward_and_cross(direction):
    if hasattr(direction, 'direction'):
        direction = direction.direction

    forward = roughly_forward(direction)
    if forward == Vector(0, 1, 0):
        cross = Vector(1, 0, 0)
    else:
        cross = Vector(forward[::-1])
    return forward, cross
