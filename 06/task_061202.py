import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94A", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]


messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"]


async def async_mess(code):
    sym = code[-1]
    ind = codes.index(code)
    if int(sym, 16) % 2 == 0:
        print("Сообщение: Неверный код, сообщение скрыто")
    else:
        print(f"Сообщение: {messages[ind]}")
    return ind


def print_code(task):
    result = task.result()
    print(f"Код: {codes[result]}")


async def main():
    for code in codes:
        task = asyncio.create_task(async_mess(code))
        task.add_done_callback(print_code)
        await task


asyncio.run(main())