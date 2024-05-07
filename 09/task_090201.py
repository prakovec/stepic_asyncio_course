import asyncio

robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']

lock = asyncio.Lock()

number_of_visits = 0

async def moving(robot_name):
    global number_of_visits
    print(f'Робот {robot_name}({number_of_visits}) передвигается к месту A')
    async with lock:
        number_of_visits += 1
        print(f'Робот {robot_name}({number_of_visits - 1}) достиг места A. Место A посещено {number_of_visits} раз')

async def main():
    tasks = [asyncio.create_task(moving(robot_name)) for robot_name in robot_names]
    await asyncio.gather(*tasks)

asyncio.run(main())