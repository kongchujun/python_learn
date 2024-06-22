import asyncio
import requests
from asycio_learn.utils.delay import async_timed

@async_timed()
async def get_example_stastus()-> int:
    return requests.get(f'https://www.baidu.com/?tn=62004195_oem_dg').status_code

@async_timed()
async def main():
    task1 = asyncio.create_task(get_example_stastus())
    task2 = asyncio.create_task(get_example_stastus())
    task3 = asyncio.create_task(get_example_stastus())

    await task1
    await task2
    await task3

asyncio.run(main())
