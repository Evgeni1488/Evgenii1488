def calculate_structure_sum(data):
    total = 0

    # Если элемент является числом (int или float)
    if isinstance(data, (int, float)):
        total += data

    # Если элемент является строкой
    elif isinstance(data, str):
        total += len(data)

    # Если элемент является списком или кортежем
    elif isinstance(data, (list, tuple)):
        for item in data:
            total += calculate_structure_sum(item)

    # Если элемент является словарем
    elif isinstance(data, dict):
        for key, value in data.items():
            total += calculate_structure_sum(key)
            total += calculate_structure_sum(value)

    # Если элемент является множеством
    elif isinstance(data, set):
        for item in data:
            total += calculate_structure_sum(item)

    return total


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99