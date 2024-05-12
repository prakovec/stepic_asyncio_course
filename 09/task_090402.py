import asyncio


wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}

storage = 0

async def gather_wood(cond, event):
    global storage
    while not event.is_set():
        await asyncio.sleep(1)
        storage += 2
        print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
        if storage in list(wood_resources_dict.values()) and storage != 0:
            async with cond:
                cond.notify()


async def craft_item(cond, event):
    global storage
    async with cond:
        for item, wood in wood_resources_dict.items():
            await cond.wait()
            if storage >= wood:
                storage -= wood
                print(f"Изготовлен {item}.")
                wood_resources_dict[item] = 0
        event.set()


async def main():
    cond = asyncio.Condition()
    event = asyncio.Event()
    await asyncio.gather(craft_item(cond, event), gather_wood(cond, event))

asyncio.run(main())