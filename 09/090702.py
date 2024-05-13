import asyncio


# Корутина для задачи прохождения барьера.
async def task(name, num, barrier):
    await asyncio.sleep(num / 10)
    print(f'{name} начинает и ожидает у барьера.')

    # Проверяем, сколько задач ожидают на барьере.
    print(f'    На барьере ожидает задач: {barrier.n_waiting + 1}')
    
    # Проверяем, сколько задач еще нужно для преодоления барьера.
    print(f'    Для прохождения нужно еще задач: {barrier.parties - (barrier.n_waiting + 1)}')
    
    # Для перехвата исключения используем try/except.
    try:
        async with barrier:
            print(f'{name} прошла через барьер.')

    except asyncio.BrokenBarrierError:
        print(f'{name} обнаружила, что барьер {["сброшен", "сломан"][barrier.broken]}.')


async def aborting_task(name, barrier):
    await asyncio.sleep(1)
    print(f'--{name} сбрасывает/ломает барьер.')
    
    # Вариант 1. Прерываем работу барьера.
    await barrier.abort()
    # Вариант 2. Сбрасываем барьер в исходное состояние.
    # await barrier.reset()



async def main():
    # Создаем барьер на 2 задачи
    barrier = asyncio.Barrier(2)
    tasks1 = [asyncio.create_task(task(f'Задача {i}', i, barrier)) for i in range(1, 4)
              ] + [asyncio.create_task(aborting_task('Сбрасывающая задача', barrier))]

    await asyncio.gather(*tasks1)
    # Создаем новый список задач.
    tasks2 = [asyncio.create_task(task(f'Задача {i}_new', i, barrier)) for i in range(1, 7)]
    
    # Проверяем состояние барьера
    print(f'--Барьер разрушен: {(state := barrier.broken)}')
    if not state:
        # Если барьер цел запускаем на него вторую партию задач
        print('--Барьер сброшен,продолжаем использовать барьер.')
    else:
        print('--Барьер сломан, все новые задачи получат BrokenBarrierError.')
        # Это для эксперимента со сломанным барьером:
        # await barrier.reset()
        # У меня барьер успешно перезапускается, но в доках написано:
        # Если барьер разрушен, возможно, лучше просто оставить его и создать новый.
    
    await asyncio.gather(*tasks2)


asyncio.run(main())