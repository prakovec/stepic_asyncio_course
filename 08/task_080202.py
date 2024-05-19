import asyncio
import random

# Создаем очереди
therapist_queue = asyncio.Queue()
surgeon_queue = asyncio.Queue()
ent_queue = asyncio.Queue()

patient_info = [
    {'name': 'Алексей Иванов', 'direction': 'Терапевт', 'procedure': 'Прием для общего осмотра'},
    {'name': 'Мария Петрова', 'direction': 'Хирург', 'procedure': 'Малая операция'},
    {'name': 'Ирина Сидорова', 'direction': 'ЛОР', 'procedure': 'Осмотр уха'},
    {'name': 'Владимир Кузнецов', 'direction': 'Терапевт', 'procedure': 'Консультация'},
    {'name': 'Елена Васильева', 'direction': 'Хирург', 'procedure': 'Хирургическая процедура'},
    {'name': 'Дмитрий Николаев', 'direction': 'ЛОР', 'procedure': 'Промывание носа'},
    {'name': 'Светлана Михайлова', 'direction': 'Терапевт', 'procedure': 'Рутинный осмотр'},
    {'name': 'Никита Алексеев', 'direction': 'Хирург', 'procedure': 'Операция на колене'},
    {'name': 'Ольга Сергеева', 'direction': 'ЛОР', 'procedure': 'Лечение ангины'},
    {'name': 'Анна Жукова', 'direction': 'Терапевт', 'procedure': 'Вакцинация'}
]

async def producer():
    for patient in patient_info:
        await asyncio.sleep(random.uniform(0, 0.5))  # имитация времени регистрации
        if patient['direction'] == 'Терапевт':
            await therapist_queue.put(patient)
        elif patient['direction'] == 'Хирург':
            await surgeon_queue.put(patient)
        elif patient['direction'] == 'ЛОР':
            await ent_queue.put(patient)
        print(f"Регистратор добавил в очередь: {patient['name']}, направление: {patient['direction']}, процедура: {patient['procedure']}")

async def consumer(doctor_type, queue):
    while True:
        patient = await queue.get()
        await asyncio.sleep(random.uniform(0, 0.5))  # имитация времени обработки
        print(f"{doctor_type} принял пациента: {patient['name']}, процедура: {patient['procedure']}")
        queue.task_done()

async def main():

    # Запускаем процесс регистрации пациентов
    task_producer = asyncio.create_task(producer())

    # Запускаем процессы приема пациентов
    task_therapist = asyncio.create_task(consumer('Терапевт', therapist_queue))
    task_surgeon = asyncio.create_task(consumer('Хирург', surgeon_queue))
    task_ent = asyncio.create_task(consumer('ЛОР', ent_queue))

    # Ждем завершения всех задач
    await task_producer
    await therapist_queue.join()
    await surgeon_queue.join()
    await ent_queue.join()

    # Отменяем задачи consumer, так как они бесконечные
    task_therapist.cancel()
    task_surgeon.cancel()
    task_ent.cancel()

# Запускаем главную функцию
asyncio.run(main())