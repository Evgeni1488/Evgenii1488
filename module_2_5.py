def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []

    # Внешний цикл для создания строк
    for i in range(n):
        # Добавляем пустую строку (список) в матрицу
        matrix.append([])
        # Внутренний цикл для заполнения строки значениями
        for j in range(m):
            matrix[i].append(value)

    # Возвращаем готовую матрицу
    return matrix


# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов на экран
print(result1)
print(result2)
print(result3)
