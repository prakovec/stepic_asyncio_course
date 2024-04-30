import asyncio


dishes = {
    'Куриный суп': 118, 
    'Бефстроганов': 13, 
    'Рататуй': 49, 
    'Лазанья': 108, 
    'Паэлья': 51, 
    'Утка по-пекински': 41, 
}


async def cook_dish(dish, duration):
    print(f"Приготовление {dish} начато.")
    await asyncio.sleep(duration * 60 / 10)
    print(f"Приготовление {dish} завершено. за {duration/10}")

async def main():
    tasks = [asyncio.create_task(cook_dish(dish, dishes[dish]), name=dish) for dish in dishes]
    done, pending = await asyncio.wait(tasks, timeout=10) 
    for p in pending:
        p.cancel()
        print(f"{p.get_name()} не успел(а,о) приготовиться и будет отменено.")

    print(f"\nПриготовлено блюд: {len(done)}. Не успели приготовиться: {len(pending)}.")


asyncio.run(main())