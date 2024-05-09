# демонстрация того, как можно синхронизировать выполнение корутин используя условия
import asyncio

async def worker(condition, msg):
    async with condition:
        print(f"worker() получил блокировку, сообщение {msg}")
        # Останавливаем выполнение корутины до тех пор, пока не получит сигнал о разблокировке
        await condition.wait()
        # Выводим сообщение о том, что корутина worker разблокирована
        print('В worker() сработал await condition.wait() и она продолжает выполнять любую логику')
        print(f"worker() разблокирована, сообщение {msg}") 

async def main():

    # Создаем объект блокировки (создаем условие)
    condition = asyncio.Condition()

    # Создаем задачу, которая выполняет корутину worker с аргументами condition и 'task1'
    task1 = asyncio.create_task(worker(condition, 'task1'))
    # Создаем задачу, которая выполняет корутину worker с аргументами condition и 'task2'
    task2 = asyncio.create_task(worker(condition, 'task2'))

    # Останавливаем выполнение корутины main на 1 секунду
    await asyncio.sleep(1)

    # Захватываем блокировку условия
    async with condition:
        # Выводим сообщение о том, что корутина main получила блокировку
        print("Корутина main получила блокировку")
        print("Корутина main реализует любую логику приложения")

        # Оповещаем все корутины, которые ждут разблокировки условия
        condition.notify_all()

        # Выводим сообщение о том, что все корутины были разблокированы
        print('main() оповещает все корутины с помощью -  condition.notify_all(), и передаёт управление в цикл событий')
        print("Корутина main разблокирована")

    # Ожидаем выполнения задач task1 и task2
    await task1
    await task2

asyncio.run(main())
