import asyncio
import random

error = None
count = 0
sek = 0

async def monitor_rocket_launches(interrupt_flag):
    global count
    global error
    global sek
    try:
        # Допишите сюда цикл
        while not error:
            await asyncio.sleep(1)
            print(f"Мониторинг ракетных запусков... (Запуск номер {count} прошёл успешно)")
            sek += 1
            error = random.random() < 0.25
            count += 1
    finally:
        # Поместите сообщение о завершении мониторинга
        print("Завершение мониторинга ракетных запусков")
        interrupt_flag.set()
        


async def main():
    global error
    global count
    global sek
    interrupt_flag = asyncio.Event()
    # Создайте Task задачу
    task = asyncio.create_task(monitor_rocket_launches(interrupt_flag))
    # Допишите сюда цикл
    while True:
        await asyncio.sleep(5)
        if count == 50:
            break
        elif error:
            print(f"Ошибка при запуске произошла на {sek} секунде =(")
            print("Отмена мониторинга ракетных запусков...")
            break
        else:
            f"Время ожидания составило {sek} секунд. За это время ошибки не произошло"
    # Запустите созданную корутину в пункте 2 через await
    await task

if __name__ == "__main__":
    asyncio.run(main())