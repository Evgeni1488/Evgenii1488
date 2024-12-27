import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    # Создаем задачи для трех силачей
    task1 = asyncio.create_task(start_strongman('Jonee', 3))
    task2 = asyncio.create_task(start_strongman('Tommy', 4))
    task3 = asyncio.create_task(start_strongman('Argon', 5))

    # Ожидаем завершения всех задач
    await task1
    await task2
    await task3


# Запуск турнира
asyncio.run(start_tournament())