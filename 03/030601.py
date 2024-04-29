import asyncio


async def simulate_long_running_task(name, delay, future: asyncio.Future):
    """Асинхронная функция, имитирующая длительную задачу."""
    print(f"Задача '{name}' началась, будет выполнена за {delay} секунд.")
    await asyncio.sleep(delay)
    result = f"Результат задачи '{name}'"
    print(f"Задача '{name}' завершена.")
    if not future.done():
        future.set_result(result)  # Устанавливаем результат для Future объекта


async def main():
    # Создаем объект Future
    future = asyncio.Future()
    
    # Запускаем корутину, передаем Future объект в функцию
    await simulate_long_running_task("Task 1", 3, future)
    
    # Получаем результат выполнения задачи
    result = future.result()
    print(f"Результат Future: {result}")


asyncio.run(main())