#!/usr/bin/env python3
'''Task 3's module.'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
  '''Executes wait_random n times.'''
  return asyncio.create_task(wait_random(max_delay))
