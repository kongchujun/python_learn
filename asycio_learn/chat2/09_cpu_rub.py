import asyncio
from asycio_learn.utils.delay import delay, async_timed

@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter

@async_timed()
async def main():
    task2 = asyncio.create_task(cpu_bound_work())
    task1 = asyncio.create_task(cpu_bound_work())
    delaytask = asyncio.create_task(delay(2))
    await task1
    await task2
    await delaytask
asyncio.run(main())