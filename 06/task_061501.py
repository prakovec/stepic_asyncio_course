import asyncio
import random


server_names = {
        "1": "Server_Alpha",
        "2": "Server_Beta",
        "3": "Server_Gamma",
        "4": "Server_Delta",
        "5": "Server_Epsilon",
    }


async def load_data(server: str) -> None:
    print(f"Загрузка данных с сервера {server} началась")
    await asyncio.sleep(random.randint(0, 5))
    print(f"Загрузка данных с сервера {server} завершена")

async def main():
    tasks = []
    for server in server_names:
        tasks.append(load_data(server_names[server]))
    await asyncio.gather(*tasks)


asyncio.run(main())