# 同时多个任务， 单个await async 无法同时运行的

import asyncio

from asycio_learn.utils.delay import delay

async def main():
    sleep_3 = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_more = asyncio.create_task(delay(3))

    await sleep_3
    await sleep_again
    await sleep_more

asyncio.run(main())