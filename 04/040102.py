import asyncio
import random


async def process_data(data):
    print(f"Received data: {data}")

    # Может включать в себя любую другую логику, которую вы хотите выполнить с полученными данными,
    # например, сохранение в базу данных, отправку уведомлений или обновление интерфейса пользователя.

# Асинхронная функция для опроса сетевого устройства
async def polling_network_device():
    while True:
        data = random.randint(0, 1000000)
        await process_data(data)

        # Здесь мы можем выполнить какие-то действия, 
        # такие как отправку запроса к устройству и получение ответа

        # Ожидание 5 секунд перед следующим опросом
        await asyncio.sleep(5)


async def main():
    task = asyncio.create_task(polling_network_device())  # Создаем задачу для опроса сетевого устройства
    await task  # Ожидаем завершения задачи

asyncio.run(main())
