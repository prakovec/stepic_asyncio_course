import asyncio
import aiofiles

import aiocsv
from aiocsv import AsyncDictReader

import json

async def main():
    result = []
    async with aiofiles.open(r"10/100905/files/address_10000.csv", mode="r", encoding="utf-8-sig", newline="") as afp:
        async for row in AsyncDictReader(afp, delimiter=";"):
            result.append(row)
    async with aiofiles.open(r"10/100905/files/result.json", mode="w", encoding="utf-8", newline="") as afout:
        await afout.write(json.dumps(result, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    asyncio.run(main())