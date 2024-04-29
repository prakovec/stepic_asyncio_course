import asyncio

news_list = [
    "Новая волна COVID-19 обрушилась на Европу",
    "Конференция разработчиков игр пройдет онлайн",
    "Открыт новый вид подводных животных",
    "Новые исследования о влиянии COVID-19 на здоровье",
    "Выставка игр E3 переходит в онлайн-формат"]

keywords = ["COVID-19", "игр", "новый вид"]


async def analyze_news(keyword, news_list, delay):
    await asyncio.sleep(delay)
    for news in news_list:
        if keyword in news:
            print(f"Найдено соответствие для '{keyword}': {news}")


async def main():
    tasks: list[asyncio.Task] = []
    # Создаем асинхронные задачи для каждой корутины с разными ключевыми словами и задержками
    for time, keyword in enumerate(keywords):
        tasks.append(asyncio.create_task(analyze_news(keyword, news_list, time - 1)))

    # Ожидаем выполнения всех задач
    await asyncio.gather(*tasks)

asyncio.run(main())