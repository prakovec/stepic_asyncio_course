import asyncio


async def publish_post(text: str) -> None:
    await asyncio.sleep(1)
    print(f"Пост опубликован: {text}")


async def notify_subscriber(subscriber):
    await asyncio.sleep(1)
    print(f"Уведомление отправлено {subscriber}")


async def notify_subscribers(subscribers):
    tasks = []

    [tasks.append(asyncio.create_task(notify_subscriber(subscriber))) for subscriber in subscribers]

    await asyncio.gather(*tasks)


async def main():
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    await publish_post(post_text)
    await notify_subscribers(subscribers)


asyncio.run(main())
