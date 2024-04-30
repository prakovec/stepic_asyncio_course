import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 2


async def portal_operator():
    portal_activation = asyncio.ensure_future(activate_portal(2))
    await portal_activation
    res = 1 if portal_activation.result() > 4 else portal_activation.result()
    teleportation = asyncio.ensure_future(perform_teleportation(res))
    await teleportation

    print(f'Результат активации портала: {res} единиц энергии\nРезультат телепортации: {teleportation.result()} единиц времени')


asyncio.run(portal_operator())