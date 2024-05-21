import asyncio
import aiofiles
from aiofiles import os as aos

import aiocsv
from aiocsv import AsyncDictReader

import json

sum_new = 0
sum_secondhand = 0

async def  read_and_sum(path):
    global sum_new, sum_secondhand
    async with sem:
        async with aiofiles.open(path, mode="r", encoding="cp1251", newline="") as afp:
                async for row in AsyncDictReader(afp, delimiter=";", quotechar='"'):
                        if row['Состояние авто'].lower() == 'б/у':
                            sum_secondhand += int(row['Стоимость авто'])
                        elif row['Состояние авто'].lower() == 'новый':
                            sum_new += int(row['Стоимость авто'])

async def sum_even_numbers_in_files(directory):
    entries = await aos.scandir(directory)
    tasks = []
    for entry in entries:
        if entry.is_file():
            tasks.append(read_and_sum(entry.path))
        else:
            tasks.append(sum_even_numbers_in_files(entry.path))

    await asyncio.gather(*tasks)
    

sem = asyncio.Semaphore(1000)
asyncio.run(sum_even_numbers_in_files(r"10/100907/files/"))
print(f"New: {sum_new}, Secondhand: {sum_secondhand}") 

with open(r"10/100907/result.json", mode="w", encoding="utf-8") as afout:
    json.dump({"Б/У": sum_secondhand, "Новый": sum_new}, afout, ensure_ascii=False, indent=4)