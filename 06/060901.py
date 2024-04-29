import asyncio


async def main_task():
    # Вывод сообщения о запуске корутины main_task
    print("Корутина main_task запустилась")
    # Задержка выполнения корутины main_task на 5 секунд
    await asyncio.sleep(5)
    # Вывод сообщения о завершении корутины main_task
    print("Корутина main_task завершилась")


async def main():
    # Создание задачи из корутины main_task и запуск ее асинхронного выполнения
    task = asyncio.create_task(main_task())
    # Задержка выполнения основной корутины main на 1 секунду
    await asyncio.sleep(1)
    # Отмена задачи (запрос на отмену выполнения корутины main_task)
    task.cancel()

    try:
        # Ожидание завершения задачи
        await task
    except asyncio.CancelledError:
        # Вывод сообщения, если задача была отменена (обработка исключения отмены задачи)
        print("Задача отменена")


# Запуск асинхронного выполнения корутины main
asyncio.run(main())