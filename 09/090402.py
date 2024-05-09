import asyncio

# Объявление корутины consumer
async def consumer(condition, name):
    # Блокировка условия
    async with condition:
        # Печатаем сообщение, что потребитель ждет
        print(f'{name} - ждет')
        # Ожидание сигнала
        await condition.wait()
        # Печатаем сообщение, что потребитель проснулся
        print(f'{name} - проснулся')

# Объявление корутины producer
async def producer(condition):
    # Блокировка условия
    async with condition:
        # Печатаем сообщение, что производитель производит
        print('Производитель производит')
        # Уведомление всех ожидающих корутин
        condition.notify_all()

async def main():
    # Создание условия
    condition = asyncio.Condition()

    # Создание списка корутин-потребителей
    consumers = [asyncio.create_task(consumer(condition, f'Потребитель {i}')) for i in range(3)]

    # Ожидание выполнения всех корутин (производителя и потребителей)
    await asyncio.gather(producer(condition), *consumers)


asyncio.run(main())