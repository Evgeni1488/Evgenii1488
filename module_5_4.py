class House:
    houses_history = []  # Атрибут класса для хранения истории

    def __new__(cls, *args, **kwargs):
        # Создание нового экземпляра объекта
        instance = super().__new__(cls)
        # Добавление названия дома в историю
        if args:  # Проверяем, есть ли позиционные аргументы
            house_name = args[0]
            cls.houses_history.append(house_name)
        return instance

    def __init__(self, name, floors):
        self.name = name  # Название дома
        self.floors = floors  # Количество этажей

    def __del__(self):
        # Вывод сообщения при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

# Пример использования класса House
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2
del h3

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаляем последний объект
del h1
