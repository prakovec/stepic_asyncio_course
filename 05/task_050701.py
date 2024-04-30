import asyncio


processors_delays = {
    'Intel Core i9-11900K': 7.01,
    'Intel Core i7-11700K': 4.32,
    'Intel Core i5-11600K': 8.59,
    'AMD Ryzen 9 5950X': 2.53,
    'AMD Ryzen 7 5800X': 5.43,
    'AMD Ryzen 5 5600X': 6.34,
    }


async def simulate_processing(delay):
    await asyncio.sleep(delay)


async def main():
    tasks = [asyncio.create_task(simulate_processing(delay), name=processor) for processor, delay in processors_delays.items()]

    done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    print(f"Первый завершенный процесс: {done.pop().get_name()}")

asyncio.run(main())