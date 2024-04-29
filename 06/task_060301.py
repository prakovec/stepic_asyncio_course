import asyncio

files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9
}

NETWORK_SPEED = 8

async def download_file(file_name, file_size):
    download_time = file_size / NETWORK_SPEED
    print(f"Начинается загрузка файла: {file_name}, его размер {file_size} мб, время загрузки составит {download_time} сек")
    await asyncio.sleep(download_time)
    print(f"Загрузка завершена: {file_name}")

async def monitor_tasks(tasks):
    while not all(task.done() for task in tasks):
        await asyncio.sleep(0.95)
        for task in tasks:
            status = "завершена" if task.done() else "в процессе"
            print(f"Задача {task.get_name()}: {status}, Статус задачи {task.done()}")


async def main():
    tasks = [asyncio.create_task(download_file(file_name, file_size), name=file_name) for file_name, file_size in files.items()]
    await asyncio.gather(*tasks, monitor_tasks(tasks))
    print("Все файлы успешно загружены")

asyncio.run(main())