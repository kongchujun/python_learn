# 下面例子显示有task和没有task的区别：

import asyncio

async def my_coroutine(duration):
    print(f"Task will run for {duration} seconds")
    await asyncio.sleep(duration)
    print(f"Task completed after {duration} seconds")

async def main():
    # 直接调用
    coroutine = my_coroutine(3)  # 这只是创建了一个协程对象
    await coroutine  # 这里实际执行协程
    
    # 使用 create_task
    task1 = asyncio.create_task(my_coroutine(3))  # 创建并调度任务
    task2 = asyncio.create_task(my_coroutine(3))  # 创建并调度任务
    await task1  # 等待任务完成
    await task2  # 等待任务完成


asyncio.run(main())
