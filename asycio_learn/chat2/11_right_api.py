import asyncio
import aiohttp
from asycio_learn.utils.delay import async_timed
import ssl
@async_timed()
async def get_example_stastus()-> int:
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE  # 关闭证书验证

    url = 'https://www.baidu.com/?tn=62004195_oem_dg'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl = ssl_context) as response:
            return await response.text()

@async_timed()
async def main():
    task1 = asyncio.create_task(get_example_stastus())
    task2 = asyncio.create_task(get_example_stastus())
    task3 = asyncio.create_task(get_example_stastus())

    await task1
    await task2
    await task3

asyncio.run(main())
