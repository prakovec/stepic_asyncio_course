import asyncio

async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    # Создаем задачи для асинхронного выполнения
    alex = asyncio.create_task(read_book('Алекс', 5))
    mary = asyncio.create_task(read_book('Мария', 3))
    ivan = asyncio.create_task(read_book('Иван', 4))
    
    # asyncio.gather(alex, mary, ivan)
    await asyncio.gather(alex, mary, ivan)


asyncio.run(main())