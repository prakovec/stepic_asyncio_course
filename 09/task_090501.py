import asyncio

request_count = 0

async def access_db(sem, user):
    global request_count
    async with sem:
        print(f"Пользователь {user} делает запрос")
        request_count += 1
        await asyncio.sleep(1)
        print(f"Запрос от пользователя {user} завершен")
        print(f"Всего запросов: {request_count}")


async def main():
    users = ["sasha", "petya", "masha", "katya", "dima", "olya", "igor", "sveta", "nikita", "lena",
         "vova", "yana", "kolya", "anya", "roma", "nastya", "artem", "vera", "misha", "liza"]

    sem = asyncio.Semaphore(3)

    tasks = [asyncio.create_task(access_db(sem, user)) for user in users]
    await asyncio.wait(tasks)

asyncio.run(main())