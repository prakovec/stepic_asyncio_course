import asyncio
import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data
        

async def process_data(data):
    print(f"Received data: {data}")

    # Может включать в себя любую другую логику, которую вы хотите выполнить с полученными данными,
    # например, сохранение в базу данных, отправку уведомлений или обновление интерфейса пользователя.

# Асинхронная функция для долгого опроса сервера
async def long_polling(url):
    while True:
        await asyncio.sleep(5)
        data = await fetch_data(url)
        if data:
            await process_data(data)


async def main():
    task = asyncio.create_task(long_polling("https://jsonplaceholder.typicode.com/posts"))  # Создаем задачу для долгого опроса сервера
    await task  # Ожидаем завершения задачи

asyncio.run(main())