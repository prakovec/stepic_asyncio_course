import asyncio
import random 


ip_dct = {'192.168.0.1': [0, 100], '192.168.0.2': [225, 300], '192.168.2.5': [150, 185]}


async def scan_port(address, port):
    """
    Асинхронная функция, имитирующая сканирование порта на заданном ip-адресе.
    """
    await asyncio.sleep(1)
    if random.randint(0, 100) == 1:
        # Печать сообщения об обнаружении открытого порта.
        print(f"Port {port} on {address} is open")
        return port



async def scan_range(address, start_port, end_port):
    """
    Асинхронная функция, проверяющая состояние диапазона портов по указанному адресу.
    """
    # Печать сообщения о начале сканирования диапазона портов для заданного ip-адреса.
    print(f"Scanning ports {start_port}-{end_port} on {address}")
    tasks = []
    range_ports = range(start_port, end_port + 1)
    for port in range_ports:
        tasks.append(asyncio.create_task(scan_port(address, port)))
    
    open_ports = [port for port in await asyncio.gather(*tasks) if port]
    return (address, open_ports)



async def main(dct):
    """
    Основная асинхронная функция, управляющая процессом сканирования портов из переданного в нее словаря.
    """
    tasks = []
    for ip, ports in dct.items():
        tasks.append(asyncio.create_task(scan_range(ip, ports[0], ports[1])))
    results = await asyncio.gather(*tasks)
   
    for result in results:
        if result[1] not in ([], None):
            # Печать сообщения о найденных открытых портах.
            print(f"Всего найдено открытых портов {len(result[1])} {result[1]} для ip: {result[0]}")


# Запуск асинхронного приложения с передачей в main() словаря ip_dct
asyncio.run(main(ip_dct))