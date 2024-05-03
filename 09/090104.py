"""
Condition (условие) - это более сложный примитив синхронизации, который можно использовать для координации работы между несколькими корутинами. Он позволяет одной корутине ждать, пока другая корутина не установит определенное условие.

Этот код демонстрирует использование примитива синхронизации Condition в библиотеке asyncio для координации работы между двумя корутинами - consumer и producer.
"""

import asyncio

# создаем экземпляр Condition
condition = asyncio.Condition()


async def consumer(condition):
    async with condition:
        print('consumer: ожидание события')
        await condition.wait()
        print('consumer: получено событие')

async def producer(condition):
    print('producer: засыпаем')
    await asyncio.sleep(1)
    print('producer: просыпаемся и устанавливаем условие')
    async with condition:
        condition.notify_all()
        print('producer: событие установлено')


async def main():
    # Запускаем consumer и producer параллельно
    await asyncio.gather(consumer(condition), producer(condition))

asyncio.run(main())