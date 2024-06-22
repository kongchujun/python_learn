import asyncio

from asycio_learn.utils.delay import delay

async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except TimeoutError:
        print('task takes too long than 5 seconds')
        result = await task
        print("in exception result is ", result)

asyncio.run(main())