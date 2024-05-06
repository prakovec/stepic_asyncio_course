"""
Во втором примере, без блокировки, мы видим, что переменную counter изменяют обе корутины - worker_1() и worker_2() - поочерёдно. Если в нашем, сильно упрощённом примере, это не так страшно, потому что мы работаем с одной переменной, то, когда вы будете работать с БД, такое поведение может вызвать критические ошибки.
"""
import asyncio

counter = 0

async def worker_1():
    global counter
    for i in range(10):
        counter += 1
        print(f"Переменная увеличена на 1 из корутины worker_1, counter = {counter}")
        await asyncio.sleep(1)

async def worker_2():
    global counter
    for i in range(10):
        counter += 1
        print(f"Переменная увеличена на 1 из корутины worker_2, counter =  {counter}")
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    await task1
    await task2

asyncio.run(main())