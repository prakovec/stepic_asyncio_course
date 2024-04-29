import asyncio


# Корутина для создания задач
async def coro():
    # Получение имени выполняемой задачи
    name = asyncio.current_task().get_name()
    # Сообщение о начале выполнения задачи
    print(f"Задача {name} начала выполнение")
    # имитация выполнения I/O операции
    await asyncio.sleep(1)
    # Сообщение о завершении выполнения задачи
    print(f"Задача {name} завершила выполнение")


# базовая корутина
async def main():
    # создания группы задач
    async with asyncio.TaskGroup() as group:
        # создание трех задач
        tasks = [group.create_task(coro(), name=f"Задача_0{i}") for i in range(1, 4)]
        # даём задачам время поработать
        await asyncio.sleep(.5)
        # отмена второй задачи
        tasks[1].cancel()
    # Проверка состояния каждой задачи
    for task in tasks:
        print(f'{task.get_name()}: done={task.done()}, cancelled={task.cancelled()}')


asyncio.run(main())