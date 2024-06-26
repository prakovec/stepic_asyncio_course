import asyncio


async def print_with_delay(num: int):
    await asyncio.sleep(1)
    print(f"Coroutine {num} is done")


async def main():
    [await asyncio.create_task(print_with_delay(i)) for i in range(10)]


asyncio.run(main())