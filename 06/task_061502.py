import asyncio
import random


async def scan_port(address, port):
    await asyncio.sleep(0.5)
    is_open = True if random.random() < 0.5 else False
    if is_open:
        print(f"Порт {port} на адресе {address} открыт")
        return port
    

async def scan_range(address, start_port, end_port):
    print(f"Сканирование портов с {start_port} по {end_port} на адресе {address}")
    tasks = []
    for port in range(start_port, end_port + 1):
        tasks.append(asyncio.create_task(scan_port(address, port)))
    
    open_ports = [port for port in await asyncio.gather(*tasks) if port]
    if len(open_ports) != 0:
        print(f"Открытые порты на адресе {address}: {open_ports}")
    else:
        print(f"Открытых портов на адресе {address} не найдено")


asyncio.run(scan_range('192.168.0.1', 80, 85))
