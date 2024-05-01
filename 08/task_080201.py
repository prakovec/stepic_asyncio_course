import asyncio


patient_info = [
    "Алексей Иванов: Прием для общего осмотра",
    "Мария Петрова: Чистка зубов",
    "Ирина Сидорова: Анализ крови",
    "Владимир Кузнецов: Рентгеновское исследование",
    "Елена Васильева: Вакцинация",
    "Дмитрий Николаев: Выписка рецепта",
    "Светлана Михайлова: Осмотр офтальмолога",
    "Никита Алексеев: Сеанс физиотерапии",
    "Ольга Сергеева: Срочный прием",
    "Анна Жукова: Регулярный контрольный осмотр"
]


async def producer(queue):
    for item in patient_info:
        await asyncio.sleep(.5)
        await queue.put(item)
        print(f"Регистратор добавил в очередь: {item}")
    await queue.put(None)


async def consumer(queue):
    while True:
        await asyncio.sleep(.5)
        item = await queue.get()
        if item is None:
            break
        print(f"Врач принял пациента: {item}")
        


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))


asyncio.run(main()) 
