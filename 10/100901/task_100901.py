
import asyncio
import aiofiles
from aiofiles import os as aos

async def read_and_sum(path):
    async with sem:
        async with aiofiles.open(path, mode='r') as f:
            data = await f.read()
        return int(data) if int(data) % 2 == 0 else 0

async def sum_even_numbers_in_files(directory):
    entries = await aos.scandir(directory)
    tasks = [read_and_sum(entry.path) for entry in entries if entry.is_file()]
    results = await asyncio.gather(*tasks)
    return sum(results)

async def main():
    directory = r'10/100901/files/'
    total = await sum_even_numbers_in_files(directory)
    print(f'Total sum of even numbers in all files: {total}')

if __name__ == '__main__':
    sem = asyncio.Semaphore(5000)

    asyncio.run(main())