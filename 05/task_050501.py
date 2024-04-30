import asyncio

# Словарь бегунов: Имя + скорость бега (м/с)
# Полный список бегунов скрыт под капотом задачи.
runners = {
    "Молния Марк": 12.8,
    "Ветреный Виктор": 13.5,
    "Скоростной Степан": 11.2,
    "Быстрая Белла": 10.8,

}

distance = 100  # Дистанция в метрах

async def run_lap(name, speed):
    time_needed = round(distance / speed, 2)
    await asyncio.sleep(time_needed)
    print(f"{name} завершил круг за {time_needed} секунд")


async def main():
    tasks = []
    for name, speed in runners.items():
        tasks.append(asyncio.create_task(run_lap(name, speed)))
    try:
        await  asyncio.wait_for(asyncio.gather(*tasks), timeout=10)
    except asyncio.TimeoutError:
        pass

asyncio.run(main())