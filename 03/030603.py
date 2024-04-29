import asyncio


async def do_some_work_1(x, future: asyncio.Future):
    print(f"Выполняется работа 1: {x}")
    await asyncio.sleep(x)
    future.set_result(x * 2)


async def do_some_work_2(x, future: asyncio.Future):
    print(f"Выполняется работа 2: {x}")
    await asyncio.sleep(x)
    future.set_result(x + 2)


async def main():
    # Создаем объекты Future для каждой задачи
    future_1 = asyncio.Future()
    future_2 = asyncio.Future()

    # Запускаем первую задачу и передаем ей Future
    asyncio.create_task(do_some_work_1(2, future_1))

    # Дожидаемся завершения первой задачи
    await future_1
    result_1 = future_1.result()

    # Запускаем вторую задачу, передавая результат первой и объект Future
    asyncio.create_task(do_some_work_2(result_1, future_2))

    # Дожидаемся завершения второй задачи
    await future_2
    result_2 = future_2.result()

    print(f"Результат future_1: {result_1}")  # Выводим результат первой задачи
    print(f"Результат future_2: {result_2}")  # Выводим результат второй задачи


asyncio.run(main())