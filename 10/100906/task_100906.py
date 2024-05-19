import asyncio
import aiofiles
from aiofiles import os as aos

import aiocsv
from aiocsv import AsyncDictReader

import json

import glob
import os

async def process_csv(path):
    
    async with sem:
        async with aiofiles.open(path, mode="r", encoding="utf-8-sig", newline="") as afp:
            async for row in AsyncDictReader(afp, delimiter=",", quotechar='"'):
                    if row['Балл ЕГЭ'] == '100':
                        res.append(row)


async def scan_dir(directory):
    files = glob.glob(os.path.join(directory, '**/*'))
    tasks = []
    for file in files:
        tasks.append(asyncio.create_task(process_csv(file)))
    await asyncio.gather(*tasks)

    sorted_result = sorted(res, key=lambda x: x['Телефон для связи'])

    async with aiofiles.open(r"10/100906/result.json", mode="w", encoding="utf-8", newline="") as afout:
        await afout.write(json.dumps(sorted_result, ensure_ascii=False, indent=4))

sem = asyncio.Semaphore(1000)
res = []
asyncio.run(scan_dir(r"10/100906/files/"))

