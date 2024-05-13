import asyncio

users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']

async def access_db(user, condition):
    
    print(f'Пользователь {user} ожидает доступа к базе данных')

    async with condition:
        await asyncio.sleep(1)
        print(f'Пользователь {user} подключился к БД')
        print(f'Пользователь {user} отключается от БД')
        condition.notify()  # Оповещаем следующего пользователя

async def main():
    condition = asyncio.Condition()

    # Создаем корутины для всех пользователей
    tasks = [access_db(user, condition) for user in users]
    # Запускаем все корутины
    await asyncio.gather(*tasks)


asyncio.run(main())