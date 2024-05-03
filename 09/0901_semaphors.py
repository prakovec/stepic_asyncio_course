import asyncio

# Создаем экземпляр Semaphore максимум c двумя разрешениями

# Поочередно выполните код с разным типом семафора, чтобы понять в чем разница

semaphore = asyncio.Semaphore(2)
# semaphore = asyncio.BoundedSemaphore(2)


async def my_coroutine(id):
    print(f'Корутина {id} хочет получить семафор')
    await semaphore.acquire()
    print(f'Корутина {id} получила семафор')
    await asyncio.sleep(1)
    semaphore.release()
    print(f'Корутина {id} отпустила семафор')
    semaphore.release()
    print(f'Корутина {id} отпустила семафор еще раз')


# Запускаем несколько корутин
async def main():
    await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))


asyncio.run(main())