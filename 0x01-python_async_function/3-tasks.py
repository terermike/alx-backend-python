#!/usr/bin/env python3
"""
Regular function that returns an asyncio.Task
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that waits for a random delay between 0 and
    max_delay (included and float value) seconds and eventually returns it.
    """
    async def wait_random(max_delay: int) -> float:
        """Waits for a random delay between 0 and max_delay seconds."""
        delay = random.uniform(0, max_delay)
        await asyncio.sleep(delay)
        return delay

    return asyncio.create_task(wait_random(max_delay))
