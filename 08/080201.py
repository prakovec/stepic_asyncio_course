import asyncio
from random import random


async def producer(queue):
    print("Производитель запущен")
    for _ in range(10): # генерация работы
        value = random() # генерация значения
        await asyncio.sleep(value) # блокировка для имитации работы
        await queue.put(value) # добавление значения в очередь
    await queue.put(None) # отправка сигнала об окончании
    print("Производитель: Done")


async def consumer(queue):
    print("Потребитель запущен")
    # выполнение работы
    while True:
        item = await queue.get() # получение элемента из очереди
        if item is None: # проверка сигнала остановки
            break
        print(f"Потребитель получил: {item}") # отчет
    print("Потребитель: Done") # всё завершено


async def main():
    # создаем общую очередь
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())