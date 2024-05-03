"""
BoundedSemaphore - работает так же, как и обычный Semaphore, но еще он не позволяет увеличить счетчик вызовами release() выше исходного значения.

Этот код демонстрирует использование примитива синхронизации BoundedSemaphore в библиотеке asyncio для ограничения количества корутин, которые могут иметь одновременный доступ к определенному ресурсу.
"""

import asyncio

# Создаем экземпляр BoundedSemaphore с максимум двумя разрешениями
semaphore = asyncio.BoundedSemaphore(2)

async def my_coroutine(id):
    print(f'Корутина {id} хочет получить семафор')
    async with semaphore:
        # Код внутри этого блока будет выполняться только двумя корутинами в один момент времени
        print(f'Корутина {id} получила семафор')
        await asyncio.sleep(1)
    print(f'Корутина {id} отпустила семафор')

# Запускаем несколько корутин
async def main():
    await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))

asyncio.run(main())