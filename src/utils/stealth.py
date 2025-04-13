import random
import asyncio
import logging

logger = logging.getLogger(__name__)

async def add_human_delay():
    """Add a random delay to simulate human behavior"""
    base_delay = random.uniform(0.5, 2.0)
    micro_delay = random.uniform(0, 0.1)
    total_delay = base_delay + micro_delay
    logger.debug(f"Adding human-like delay: {total_delay:.2f}s")
    await asyncio.sleep(total_delay) 