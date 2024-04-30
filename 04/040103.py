import asyncio


async def print_message():
    while True:
        print("Имитация работы функции")
        await asyncio.sleep(1)


async def interrupt_handler(interrupt_flag: asyncio.Event):
    while True:
        # Если interrupt_flag установлен Выводим сообщение о прерывании
        await asyncio.sleep(0.5)
        if interrupt_flag.is_set():
            print("Произошло прерывание!, в этом месте может быть установлен любой обработчик")

            # Очищаем interrupt_flag
            interrupt_flag.clear()
            break

async def main():
    # Создаем флаг interrupt_flag с помощью asyncio.Event
    interrupt_flag = asyncio.Event()

    # Создаем задачу исполняющую функцию print_message
    asyncio.create_task(print_message())   # Создаем задачу task1 исполняющую функцию print_message
    task2 = asyncio.create_task(interrupt_handler(interrupt_flag))  # Создаем задачу task2 исполняющую функцию interrupt_handler
    while True:
        await asyncio.sleep(3)
        # Устанавливаем interrupt_flag
        interrupt_flag.set()
        await task2
        task2 = asyncio.create_task(interrupt_handler(interrupt_flag))

asyncio.run(main())