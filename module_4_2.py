# Определяем функцию test_function
def test_function():
    # Внутри test_function создаем inner_function
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызываем inner_function внутри test_function
    inner_function()


# Вызываем test_function
test_function()

# Попытка вызвать inner_function вне test_function
try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    return inner_function

# Сохраняем inner_function в переменную
my_func = test_function()

# Теперь можно вызвать inner_function
my_func()