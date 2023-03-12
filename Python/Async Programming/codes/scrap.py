import time 
import random
import asyncio

async def func_1(n:int):
    print(f'\t sleeping for {n} sec')
    asyncio.sleep(n)

async def func_2(n:int):
    print(time.time())
    await func_1(n)
    print(time.time())


for _ in range(10):
    n = random.randint(1,5)
    asyncio.run(func_2(n))