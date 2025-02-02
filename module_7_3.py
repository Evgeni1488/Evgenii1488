import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем имена файлов

    def get_all_words(self):
        all_words = {}  # Словарь для хранения слов из всех файлов
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']  # Список пунктуации для удаления

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()  # Чтение файла и перевод в нижний регистр
                # Удаление пунктуации
                for p in punctuation:
                    text = text.replace(p, ' ')
                # Разделение текста на слова
                words = text.split()
                # Сохранение слов в словарь
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        result = {}
        all_words = self.get_all_words()  # Получаем словарь всех слов

        for file_name, words in all_words.items():
            try:
                # Находим индекс первого вхождения слова
                index = words.index(word)
                result[file_name] = index + 1  # Добавляем 1, так как индексация начинается с 0
            except ValueError:
                # Если слово не найдено, пропускаем файл
                pass

        return result

    def count(self, word):
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        result = {}
        all_words = self.get_all_words()  # Получаем словарь всех слов

        for file_name, words in all_words.items():
            # Считаем количество вхождений слова
            count = words.count(word)
            if count > 0:
                result[file_name] = count

        return result


# Пример использования
if __name__ == "__main__":
    # Создаем объект WordsFinder
    finder = WordsFinder('test_file.txt')

    # Пример вывода всех слов
    print(finder.get_all_words())

    # Пример поиска первого вхождения слова
    print(finder.find('TEXT'))

    # Пример подсчета количества вхождений слова
    print(finder.count('teXT'))