import asyncio


max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0
}


async def counter(counter_name: str, delay: int, max_count: int):
    while counters[counter_name] < max_count:
        await asyncio.sleep(delay)
        counters[counter_name] += 1
        print(f"{counter_name}: {counters[counter_name]}")


async def main():
    tasks = []
    for counter_name, max_count in max_counts.items():
        tasks.append(asyncio.create_task(counter(counter_name, 1, max_count)))

    await asyncio.gather(*tasks)

asyncio.run(main())