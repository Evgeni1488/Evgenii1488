# Глобальная переменная для подсчёта вызовов
calls = 0

# Функция для подсчёта вызовов
def count_calls():
    global calls
    calls += 1

# Функция для получения информации о строке
def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case

# Функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    return string.lower() in [item.lower() for item in list_to_search]

# Примеры вызовов функций
print(string_info("Hello, World!"))  # Вывод: (13, 'HELLO, WORLD!', 'hello, world!')
print(is_contains("UrbaN", ["urban", "rural", "city"]))  # Вывод: True
print(string_info("Python"))  # Вывод: (6, 'PYTHON', 'python')
print(is_contains("Java", ["python", "c++", "javascript"]))  # Вывод: False

# Вывод значения переменной calls
print(f"Функции были вызваны {calls} раз(а).")

