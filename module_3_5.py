def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Отделяем первую цифру и преобразуем её в целое число
        first = int(str_number[0])
        # Если первая цифра равна 0, пропускаем её
        if first == 0:
            return get_multiplied_digits(int(str_number[1:]))
        # Возвращаем произведение первой цифры и рекурсивного вызова с оставшимися цифрами
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки 1, возвращаем единственную цифру, если она не равна 0
        return int(str_number) if str_number != '0' else 1  # Возвращаем 1 для нуля, чтобы не умножать на 0


# Примеры вызовов функции
result = get_multiplied_digits(40203)
print(result)  # Ожидаемый вывод: 24

result2 = get_multiplied_digits(402030)
print(result2)  # Ожидаемый вывод: 24