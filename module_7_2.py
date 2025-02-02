def custom_write(file_name, strings):
    strings_positions = {}  # Словарь для хранения позиций строк
    with open(file_name, 'w', encoding='utf-8') as file:  # Открываем файл с кодировкой utf-8
        for i, string in enumerate(strings, start=1):
            # Получаем текущую позицию курсора (начало строки)
            byte_position = file.tell()
            # Записываем строку в файл с добавлением '\n'
            file.write(string + '\n')
            # Сохраняем информацию в словарь
            strings_positions[(i, byte_position)] = string
    return strings_positions


# Пример использования
if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)