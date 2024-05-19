import asyncio
import json
import aiofiles
from aiofiles import os as aos


async def read(file, dct):
    async with sem:
        async with aiofiles.open(f"10//100902//files//{file}", "r", encoding='utf-8') as f:
            for line in await f.readlines():
                name, message = line.split('-')[-1].strip().split(': ')
                dct[name] = dct.setdefault(name, 0) + len(message)


async def main():
    dct = dict()
    await asyncio.gather(*[read(filename, dct) for filename in await aos.listdir("10//100902//files//")])

    dct = {k: f"{round(v * 0.03, 2)}р" for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}
    print(json.dumps(dct, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    sem = asyncio.Semaphore(5000)
    asyncio.run(main())