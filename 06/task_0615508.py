import asyncio
import itertools
import random


shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]


async def launch_firework(color, shape, action):
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")

async def main():
    combinations = list(itertools.product(colors, shapes, actions))
    tasks = [asyncio.create_task(launch_firework(*combination)) for combination in combinations]

    await asyncio.gather(*tasks) 


asyncio.run(main())