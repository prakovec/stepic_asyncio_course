import asyncio


# Корутина worker, принимающая объект asyncio.Barrier.
async def worker(barrier: asyncio.Barrier, num):
    print(f"worker_{num} ждет на барьере")

    # В этой точке выполнение задачи приостанавливается
    # до момента накопления на барьере заданного количества задач.
    await barrier.wait()
    # После преодоления барьера работа задачи возобновляется.

    await asyncio.sleep(0.5)
    # Вывод сообщения о прохождении барьера worker-ом.
    print(f"worker_{num} прошел барьер")


async def main():
    # Создание объекта asyncio.Barrier (для разблокировки ожидаем 4 задачи).
    barrier = asyncio.Barrier(4)
    tasks = [asyncio.create_task(worker(barrier, num)) for num in range(3)]

    print(f'Состояние {barrier=}')
    print("Ждем, пока worker's пройдут барьер")
    await asyncio.sleep(0)
    print(f'Состояние {barrier=}')

    # Регистрируем на нашем барьере последнюю, 4-ю задачу для преодоления барьера.
    await barrier.wait()

    # Часть кода которая может быть выполнена только после преодоления барьера.
    # Имитация выполнения длительной I/O операции.
    await asyncio.sleep(1)
    print("Все задачи успешно прошли барьер")
    print(f'Состояние {barrier=}')


asyncio.run(main())