def generate_password(n):
    pairs = []  # Список для хранения пар
    used_numbers = set()  # Множество для отслеживания использованных чисел

    # Перебираем все возможные пары чисел от 1 до 20
    for i in range(1, 21):
        for j in range(1, 21):
            # Проверяем, что числа не использовались ранее и их сумма делит n без остатка
            if i not in used_numbers and j not in used_numbers and (i + j) != 0 and n % (i + j) == 0:
                pairs.append((i, j))  # Добавляем пару в список
                used_numbers.add(i)   # Добавляем числа в множество использованных
                used_numbers.add(j)

    # Формируем пароль из найденных пар
    password = ''.join([f"{pair[0]}{pair[1]}" for pair in pairs])
    return password

# Примеры использования
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = generate_password(n)
    print(f"Пароль для числа {n}: {result}")
else:
    print("Число должно быть от 3 до 20.")