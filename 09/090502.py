from random import random
import asyncio


async def task(semaphore, number):
    async with semaphore:  # Используется контекстный менеджер, чтобы автоматически освободить семафор после использования
        value = random()  # Используем функцию random() для получения случайного значения от 0 до 1
        await asyncio.sleep(value)  # Приостанавливаем выполнение корутины на случайное количество времени
        print(f'Задача {number} получила {value}')  # Информируем о полученном случайном значении


async def main():
    semaphore = asyncio.Semaphore(2)  # Ограничиваем количество одновременно выполняемых задач до двух
    tasks = [asyncio.create_task(task(semaphore, i)) for i in range(10)]  # Создаем список из 10 асинхронных задач
    await asyncio.wait(tasks)  # Ожидаем завершения всех задач, используя функцию asyncio.wait

# Запускаем asyncio программу
asyncio.run(main())