#!/usr/bin/env python3
"""
This module defines an asynchronous routine that spawns multiple
coroutines of wait_random.
"""

import asyncio
from typing import List
from 0-basic_async_syntax0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn n coroutines of wait_random with the specified max_delay and
    return the list of delays.

    Args:
        n: The number of coroutines to spawn.
        max_delay: The maximum delay in seconds for each coroutine.

    Returns:
        The list of random delays in seconds (float values) in ascending order
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)
    return sorted(results)
