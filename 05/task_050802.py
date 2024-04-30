import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 2


async def recharge_portal(x):
    print(f"Подзарядка портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 3


async def check_portal_stability(x):
    print(f"Проверка стабильности портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 4


async def restore_portal(x):
    print(f"Восстановление портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 5


async def close_portal(x):
    print(f"Закрытие портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x - 1


async def portal_operator():
    x = 1
    portal_activation = asyncio.ensure_future(activate_portal(x + 1))
    portal_teleportation = asyncio.ensure_future(perform_teleportation(x + 2))
    portal_recharge = asyncio.ensure_future(recharge_portal(x * 4))
    portal_cheking = asyncio.ensure_future(check_portal_stability(x + 4))
    portal_restore = asyncio.ensure_future(restore_portal(x + 5))
    portal_close = asyncio.ensure_future(close_portal(x + 6))

    await portal_activation
    await asyncio.gather(portal_teleportation, portal_recharge, portal_cheking, portal_restore)
    await portal_close

    print(f'Результат активации портала: {portal_activation.result()} единиц энергии\n'
            f'Результат телепортации: {portal_teleportation.result()} единиц времени\n'
            f'Результат подзарядки портала: {portal_recharge.result()} единиц энергии\n'
            f'Результат проверки стабильности: {portal_cheking.result()} единиц времени\n'
            f'Результат восстановления портала: {portal_restore.result()} единиц энергии\n'
            f'Результат закрытия портала: {portal_close.result()} единиц времени')
    

asyncio.run(portal_operator())