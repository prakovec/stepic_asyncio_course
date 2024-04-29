import asyncio


# Асинхронная функция, имитирующая асинхронную операцию
async def async_operation():
    print("Асинхронная операция началась...")
    await asyncio.sleep(2)
    print("Асинхронная операция завершена.")
    return "Результат асинхронной операции"


# Callback-функция, которая вызывается по завершении асинхронной операции
def on_completion(task):
    # Получение результата из задачи
    result = task.result()
    print(f"Callback функция вызвана. Получен результат: {result}")


# Основная асинхронная функция
async def main():
    # Создание задачи из асинхронной функции async_operation
    task = asyncio.create_task(async_operation())
    # Регистрация callback-функции для выполнения по завершении асинхронной операции   
    task.add_done_callback(on_completion)
    # Ждем завершения задачи
    await task


# Запуск основной асинхронной функции
asyncio.run(main())