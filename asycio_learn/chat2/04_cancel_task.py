# how to cancel a task
# 跟我想象的有点出入， 这里没有启动任务的， 它只是给任务设置上cancel而已

import asyncio
from asyncio import CancelledError
from asycio_learn.utils.delay import delay

async def main():
    long_task = asyncio.create_task(delay(10))
    verify_tag = 0
    while not long_task.done():
        print(f'Task not fiished')
        await asyncio.sleep(1)
        verify_tag = verify_tag + 1
        if verify_tag == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print("our task is cancelled")

asyncio.run(main())