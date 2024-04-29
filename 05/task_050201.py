import asyncio


# Пример данных
log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5}
]


async def fetch_log(event):
    await asyncio.sleep(event["delay"])
    return f"Событие: '{event['event']}' обработано с задержкой {event['delay']} сек." 


async def main():
    tasks = [asyncio.create_task(fetch_log(event)) for event in log_events]
    results = await asyncio.gather(*tasks)
    print("\n".join(results))

if __name__ == "__main__":
    asyncio.run(main())