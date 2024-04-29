import asyncio


students = {
    "Алекс": {"course": "Асинхронный Python", "step": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "step": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "step": 491, "speed": 57}
}

'''
course — название курса, который проходит студент.
step — общее количество степов в курсе.
speed — скорость чтения студента в степах в час.

reading_time = step / speed
'''

async def study_course(student, course, step, speed):
    print(f"{student} начал проходить курс {course}.")
    reading_time = step / speed
    await asyncio.sleep(reading_time)
    print(f"{student} прошел курс {course} за {round(reading_time, 2)} ч.")


async def main():
    # Создание задач с помощью asyncio.create_task для каждого студента
    tasks = []
    for student, info in students.items():
        course = info["course"]
        step = info["step"]
        speed = info["speed"]
        tasks.append(asyncio.create_task(study_course(student, course, step, speed)))

    # Ожидание завершения каждой задачи индивидуально
    for task in tasks:
        await task


asyncio.run(main())