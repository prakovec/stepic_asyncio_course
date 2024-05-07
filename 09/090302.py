"""
Пример посложнее: корутина number_generator() генерирует числа от 1 до 100 и останавливает выполнение при наступлении события i = 33.
"""

import asyncio
import random

# Создаем событие
event = asyncio.Event()


# Определяем корутину number_generator, которая генерирует случайные числа
async def number_generator():
    
    # Генерируем список из 5000 случайных чисел от 1 до 100
    lst = [random.randint(1,100) for x in range(5000)]
    
    # Перебираем сгенерированный список
    for en, i in enumerate(lst):
        
        # Ждем от 0 до 0.1 секунды
        await asyncio.sleep(random.uniform(0, .1))
        
        # Если число равно 33, устанавливаем событие
        if i == 33:
            event.set()
            
        # Выводим номер генерируемого числа
        print(f"Генерируем число: {i}")
        
        # Если событие установлено, выходим из цикла
        if event.is_set():
            
            # Выводим сообщение, что число найдено и за сколько попыток
            print(f'Событие наступило, число {i} найдено, через {en} попыток')
            break

# Определяем функцию main, которая запускает number_generator через asyncio.gather
async def main():
    await asyncio.gather(number_generator())

# Запускаем функцию main через asyncio.run
asyncio.run(main())