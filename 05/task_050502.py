import asyncio

spells = {
    "Огненный шар": 1,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Восстановление": 5,
    "Телепортация": 7,
}

true_mag = True

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]

# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды

async def cast_spell(student, spell, cast_time):
    await asyncio.sleep(cast_time)
    return student, spell, cast_time, cast_time <= max_cast_time

async def main():
    tasks = []
    for student in students:
        for spell, cast_time in spells.items():
            task = asyncio.create_task(cast_spell(student, spell, cast_time))
            tasks.append(task)

    for task in tasks:
        try:
            student, spell, cast_time, completed_in_time = await asyncio.wait_for(task, timeout=max_cast_time)
            if completed_in_time:
                print(f"{student} успешно кастует {spell} за {cast_time} сек.")
            else:
                print(f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield.")
        except asyncio.TimeoutError:
            print(f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield.")


asyncio.run(main())