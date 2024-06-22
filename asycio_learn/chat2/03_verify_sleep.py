import asyncio
# 下面的代码经过12秒， 明显也是只是一个协程
async def main():
    await asyncio.sleep(3)
    await asyncio.sleep(3)
    await asyncio.sleep(3)
    await asyncio.sleep(3)

asyncio.run(main())