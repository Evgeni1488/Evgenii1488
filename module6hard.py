import math

# Базовый класс Figure
class Figure:
    sides_count = 0  # Количество сторон (по умолчанию 0)

    def __init__(self, color, *sides):
        self.__color = list(color)  # Цвет в формате RGB
        self.filled = True  # Закрашенный (по умолчанию True)
        self.__sides = self.__validate_sides(sides)  # Стороны фигуры

    def __validate_sides(self, sides):
        # Если количество сторон не совпадает с sides_count, создаем список из единиц
        if len(sides) != self.sides_count:
            return [1] * self.sides_count
        # Проверяем, что все стороны положительные целые числа
        if all(isinstance(side, int) and side > 0 for side in sides):
            return list(sides)
        return [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        # Проверяем, что все значения RGB находятся в диапазоне от 0 до 255
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        # Проверяем, что все стороны положительные целые числа и их количество совпадает
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        # Возвращаем периметр фигуры (сумму всех сторон)
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


# Класс Circle (наследуется от Figure)
class Circle(Figure):
    sides_count = 1  # У круга одна сторона (длина окружности)

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        # Радиус круга = длина окружности / (2 * π)
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        # Площадь круга = π * r^2
        return math.pi * (self.__radius ** 2)


# Класс Triangle (наследуется от Figure)
class Triangle(Figure):
    sides_count = 3  # У треугольника три стороны

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        # Площадь треугольника по формуле Герона
        a, b, c = self.get_sides()
        p = (a + b + c) / 2  # Полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


# Класс Cube (наследуется от Figure)
class Cube(Figure):
    sides_count = 12  # У куба 12 рёбер

    def __init__(self, color, *sides):
        # Если передана одна сторона, создаем список из 12 одинаковых сторон
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        # Объём куба = сторона^3
        return self.get_sides()[0] ** 3


# Проверка работы классов
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())  # 216