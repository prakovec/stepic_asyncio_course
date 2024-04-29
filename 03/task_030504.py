import asyncio

# Словарь с максимальными значениями для каждого счётчика

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}


async def counter(counter_name: str, delay: int, max_count: int):
    counters = {counter_name: 0}
    while counters[counter_name] < max_count:
        await asyncio.sleep(delay)
        counters[counter_name] += 1
        print(f"{counter_name}: {counters[counter_name]}")


async def main():
    for counter_name, max_count in max_counts.items():
        await asyncio.create_task(counter(counter_name, delays[counter_name], max_count))

   

asyncio.run(main())