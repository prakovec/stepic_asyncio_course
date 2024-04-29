import asyncio


async def raise_exception():
    # Генерируем ошибку RuntimeError с сообщением "--Установленное исключение--"
    raise RuntimeError("--Установленное исключение--")

# Определяем асинхронную функцию main
async def main():
    # Создаем асинхронное задание, выполняющее функцию raise_exception()
    task = asyncio.create_task(raise_exception())
    # Ожидаем 0.1 секунды, позволяя другим задачам выполняться
    await asyncio.sleep(0.1)
    # Обработка исключений в блоке try-except
    try:
        # Ожидаем завершения задания task
        await task
    # Обработка исключения типа Exception
    except Exception as e:
        # Вывод сообщения с информацией о пойманном исключении
        print(f"Пойманное исключение: {e}")                 
    # Получаем исключение, которое возникло во время выполнения задания (если оно возникло)
    exception = task.exception()
    # Если исключение возникло, выводим его, или при необходимости обрабатываем
    if exception:
        print(f"Тут можно обработать возникшее исключение: {exception}")


asyncio.run(main())