import asyncio

ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]

event = asyncio.Event()


async def wait_for_alarm(num, ip):
    print(f'Датчик {num} IP-адрес {ip} настроен и ожидает срабатывания')
    await event.wait()
    print(f'Датчик {num} IP-адрес {ip} активирован, "Wee-wee-wee-wee"')

async def activation_sensor():
    await asyncio.sleep(5)
    print(f'Датчики зафиксировали движение')
    event.set()

async def main():
    sensors = [wait_for_alarm(num, ip) for num, ip in enumerate(ip)]
    await asyncio.gather(activation_sensor(), *sensors)


asyncio.run(main())