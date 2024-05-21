import asyncio
import aiofiles
from aiofiles import os as aos

import aiocsv
from aiocsv import AsyncDictWriter

import json
from datetime import datetime

res = []

async def read_data(file):
    global res
    async with aiofiles.open(file, mode="r", encoding="utf-8", newline="") as afp:
        data = await afp.read()
        dict_data = json.loads(data)
        for row in dict_data:
            if row['HTTP-статус'] == 200:
                row['Время и дата'] = int(datetime.strptime(row['Время и дата'], "%Y-%m-%d %H:%M:%S").timestamp())
                res.append(row)
        return res


async def main():
    global res
    files = await aos.listdir("10/100908/files/")
    tasks = [read_data(f"10/100908/files/{file}") for file in files]
    await asyncio.gather(*tasks)
    
    results = sorted(res, key=lambda x: x['Время и дата'])
    
    for r in results:
        dt = datetime.fromtimestamp(r['Время и дата'])
        r['Время и дата'] = dt.strftime("%d.%m.%Y %H:%M:%S")

    async with aiofiles.open(r"10/100908/res.csv", mode="w", encoding="utf-8-sig", newline="") as afp:
        writer = AsyncDictWriter(afp, list(results[0].keys()), restval="NULL", delimiter=";", lineterminator="\n")
        await writer.writeheader()
        for row in results:
            await writer.writerow(row)

asyncio.run(main())