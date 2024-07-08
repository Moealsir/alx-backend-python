#!/usr/bin/env python3
'''Task 2's module.'''
import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Executes wait_n and measures the total execution time.'''
    start = asyncio.get_event_loop().time()
    asyncio.get_event_loop().run_until_complete(wait_n(n, max_delay))
    end = asyncio.get_event_loop().time()
    return end - start
