import asyncio


async def wait_for_materials(delivery_time, future: asyncio.Future):
    """
    Асинхронная функция, имитирующая ожидание доставки строительных материалов.
    delivery_time - время, необходимое для доставки материалов.
    """

    print(f"Ожидание доставки материалов. Доставка займет {delivery_time} секунд.")
    await asyncio.sleep(delivery_time)  # Имитация задержки доставки
    print("Материалы доставлены.")
    if not future.done():
        future.set_result("Доставка завершена")


async def manage_construction_project():
    """
    Менеджер строительного проекта, который ожидает поставку материалов,
    прежде чем продолжить работу над проектом.
    """

    # Создание Future объекта
    future_materials_delivery = asyncio.Future()

    # Инициирование ожидания доставки материалов
    asyncio.create_task(wait_for_materials(5, future_materials_delivery))

    # Вы можете здесь добавить другие задачи, которые могут выполняться параллельно

    # Ожидание результата Future
    await future_materials_delivery

    # Получение и вывод результата доставки
    delivery_result = future_materials_delivery.result()
    print(f"Результат доставки: {delivery_result}")

    # После доставки можно продолжить работы над проектом
    print("Продолжение строительных работ.")


asyncio.run(manage_construction_project())