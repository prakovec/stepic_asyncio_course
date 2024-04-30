import asyncio

books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": False
    },
    ]


async def check_book(book):
    await asyncio.sleep(1)
    if not book["Наличие на полке"]:
        return book
    


async def main():
    tasks = [asyncio.create_task(check_book(book)) for book in books_json]
    results = await asyncio.gather(*tasks)
    
    [print(f"{result['Порядковый номер']}: {result['Автор']}: {result['Название']} ({result['Год издания']})") for result in results if result]


asyncio.run(main())

 