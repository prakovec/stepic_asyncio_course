import asyncio


semaphore = asyncio.Semaphore(1)  # Семафор используется для ограничения количества корутин, которые могут одновременно иметь доступ к критическому участку кода. В данном случае, мы устанавливаем ограничение в одну корутину, что позволяет защитить запись в файл от одновременного доступа.

async def write_to_file(text):
    async with semaphore:  # Конструкция async with используется для автоматического приобретения и освобождения семафора. Это позволяет обеспечить безопасность кода при работе с ресурсами, которые требуют синхронизации доступа.
        with open('file.txt', 'a', encoding='utf-8') as file:
            file.write(text)  # Метод write() используется для записи текста в файл. В данном случае, мы записываем переданный текст в файл.


async def main():
    # Создаем список корутин
    tasks = [write_to_file("строка 1\n"), write_to_file("строка 2\n"), write_to_file("строка 3\n")]
    asyncio.gather(*tasks)  # Функция gather() используется для запуска нескольких корутин одновременно. В данном случае, мы запускаем все корутины из списка tasks.


asyncio.run(main())