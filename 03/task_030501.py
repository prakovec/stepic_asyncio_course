import asyncio


async def my_coroutine1():
    print('Coroutine 1 is done')

async def my_coroutine2():
    print('Coroutine 2 is done')

async def my_coroutine3():
    print('Coroutine 3 is done')

async def main():
    task1 = asyncio.create_task(my_coroutine1())
    task2 = asyncio.create_task(my_coroutine2())
    task3 = asyncio.create_task(my_coroutine3())
    
    asyncio.gather(task1, task2, task3)

asyncio.run(main())