"""
Event - это примитив синхронизации, который позволяет одной корутине сигнализировать другим о том, что произошло какое-то событие. Корутины, которые ожидают события, будут приостановлены до тех пор, пока событие не будет установлено.

Этот код демонстрирует использование примитива синхронизации Event в библиотеке asyncio для ожидания и установки события между корутинами.
"""

import asyncio

# создаем экземпляр Event
event = asyncio.Event()


async def waiter():
    print('waiter: ожидание события')
    await event.wait()
    print('waiter: событие произошло')


async def setter():
    print('setter: засыпаем')
    await asyncio.sleep(1)
    print('setter: просыпаемся и устанавливаем событие')
    event.set()


async def main():
    # Запускаем waiter и setter параллельно
    await asyncio.gather(waiter(), setter())

asyncio.run(main())