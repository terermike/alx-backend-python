#!/usr/bin/env python3
"""Async Generator"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Coroutine that generates 10 random float values between 0 and 10 after
    each second asynchronously.

    Args:
        None

    Yields:
        float: a random float value between 0 and 10
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
