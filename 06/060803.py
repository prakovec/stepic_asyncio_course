import asyncio

# Асинхронная функция, обрабатывающая один элемент списка
async def process_item(item):
    if item == 13 or item == 'i':
        try:

        # Если элемент равен числу 13 или букве 'i', вызываем исключение ValueError
            raise ValueError(f"Обработка исключения для элемента: {item}")
        
        except ValueError as _ex:
            print(_ex)

    print(f"Элемент соответствует условию: {item}")
    return item

# Асинхронная функция, обрабатывающая список элементов
async def process_list(items):
    # Создаем асинхронные задачи для каждого элемента списка с помощью list comprehension
    tasks = [asyncio.create_task(process_item(item)) for item in items]
    # Цикл для обработки каждой задачи
    for task in tasks:
        try:
            # Если задача успешно завершена, получаем результат
            await task
        except ValueError as e:
            # Если задача вызывает исключение ValueError, устанавливаем исключение для задачи и выводим сообщение
            task.set_exception(ValueError(f'Установленное исключение {e}'))
            print(e)

# Асинхронная функция для запуска обработки списка
async def main():
    # Список элементов для обработки
    items = [13, 2, 13, 4, 13, 'a', 'b', 'c', 'i', 13, 6, 7, 8, 13, 10, 11, 13, 'i', 'e', 'f', 'i', 'h']
    # Запускаем обработку списка
    await process_list(items)


asyncio.run(main())