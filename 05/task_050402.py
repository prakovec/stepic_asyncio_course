import asyncio


theme_messages = {'Квест на поиск сокровищ': 'Найди скрытые сокровища!',
                  'Побег от дракона': 'Беги быстрее, дракон на хвосте!'
                  }

async def countdown(name, seconds):
    while seconds > 0:
        print(f"{name}: Осталось {seconds} сек. {theme_messages[name]}")
        await asyncio.sleep(1)
        seconds -= 1
    print(f"{name}: Задание выполнено! Что дальше?")
    

async def main():
    treasure_hunt = asyncio.create_task(countdown('Квест на поиск сокровищ', 10))
    dragon_escape = asyncio.create_task(countdown('Побег от дракона', 5))

    await asyncio.gather(treasure_hunt, dragon_escape)


asyncio.run(main())