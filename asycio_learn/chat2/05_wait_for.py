import asyncio

from asycio_learn.utils.delay import delay

async def main():
    long_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(long_task, timeout=1)
        print(result)
    except asyncio.TimeoutError:
        print('timeout')
        print(f'task timed out cancel ?{long_task.cancelled()}')

asyncio.run(main())
