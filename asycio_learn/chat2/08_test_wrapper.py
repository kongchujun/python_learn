import asyncio
from asycio_learn.utils.delay import async_timed

@async_timed()
async def delay(seconds:int) -> int:
    print(f"sleeping for {seconds} seconds...")
    await asyncio.sleep(seconds)
    print(f"finished for {seconds} seconds...")
    return seconds

@async_timed()
async def main():
    task_01 = asyncio.create_task(delay(2))
    task_02 = asyncio.create_task(delay(2))

    await task_01
    await task_02

asyncio.run(main())

