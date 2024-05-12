import asyncio

class Resource:
    def __init__(self, resources_dict):
        self.amount = 0
        self.resources_dict = resources_dict
        self.condition = asyncio.Condition()

    async def gather(self, gather_amount, resource_name):
        while not all(value == 0 for value in self.resources_dict.values()):
            async with self.condition:
                self.amount += gather_amount
                self.condition.notify_all()
                print(f'Добыто {gather_amount} ед. {resource_name}. На складе {self.amount} ед.')
            await asyncio.sleep(1)

    async def craft_items(self, resource_name):
        for item, amount in self.resources_dict.items():
            async with self.condition:
                while self.amount < amount:
                    await self.condition.wait()
                self.amount -= amount
                self.resources_dict[item] = 0
            print(f'Изготовлен {item} из {resource_name}.')

stone_resources_dict = {
    'Каменная плитка': 10,
    'Каменная ваза': 40,
    'Каменный столб': 50,
}

metal_resources_dict = {
    'Металлическая цепь': 6,
    'Металлическая рамка': 24,
    'Металлическая ручка': 54,
}

cloth_resources_dict = {
    'Тканевая занавеска': 8,
    'Тканевый чехол': 24,
    'Тканевое покрывало': 48,
}

stone = Resource(stone_resources_dict)
metal = Resource(metal_resources_dict)
cloth = Resource(cloth_resources_dict)

async def gather_stone():
    await stone.gather(10, 'камня')

async def gather_metal():
    await metal.gather(6, 'металла')

async def gather_cloth():
    await cloth.gather(8, 'ткани')

async def craft_stone_items():
    await stone.craft_items('камня')

async def craft_metal_items():
    await metal.craft_items('металла')

async def craft_cloth_items():
    await cloth.craft_items('ткани')

async def main():
    await asyncio.gather(
        gather_stone(), craft_stone_items(),
        gather_metal(), craft_metal_items(),
        gather_cloth(), craft_cloth_items()
    )

asyncio.run(main())