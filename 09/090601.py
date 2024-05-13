import asyncio

# Создаем экземпляр семафора с лимитом одновременных доступов == 2.
# Внимание!!! Ниже строки использующие различные типы семафора.
# Поочередно выполните код с каждым из них, чтобы понять различие в их работе


# semaphore = asyncio.Semaphore(2)
semaphore = asyncio.BoundedSemaphore(2)

print(f'Исходный лимит для {type(semaphore).__name__}: {semaphore._value}')


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
    try:
        await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))
    # Перехват исключения для ситуации, когда слишком много release()
    except ValueError:
        print(f'Попытка несанкционированного release().\n'
              f'Количество попыток освободить семафор превышает количество его захватов')
    finally:
        print(f'Лимит {type(semaphore).__name__}: {semaphore._value} ', end='/')
        print(f'(Лимит был увеличен)' if semaphore._value > 2 else f'(Увеличения лимита не произошло)')


asyncio.run(main())