import asyncio


async def monitor_cpu(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(1)


async def monitor_memory(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(1)


async def monitor_disk_space(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(1)


async def main():
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо","Катастрофически",
        "Критично"
    ]

    task1 = asyncio.create_task(monitor_cpu(status_list), name="CPU")
    task2 = asyncio.create_task(monitor_memory(status_list), name="Память")
    task3 = asyncio.create_task(monitor_disk_space(status_list), name="Дисковое пространство")

    await asyncio.gather(task1, task2, task3)
asyncio.run(main())