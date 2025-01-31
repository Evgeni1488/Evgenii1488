class Vehicle:
    # Атрибут класса: допустимые цвета
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Владелец (можно менять)
        self.__model = model  # Модель (нельзя менять)
        self.__engine_power = engine_power  # Мощность двигателя (нельзя менять)
        self.__color = color  # Цвет (нельзя менять напрямую)

    # Метод для получения модели
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод для получения мощности двигателя
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод для получения цвета
    def get_color(self):
        return f"Цвет: {self.__color}"

    # Метод для вывода информации о транспорте
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    # Метод для изменения цвета
    def set_color(self, new_color):
        # Проверяем, есть ли новый цвет в списке допустимых (без учета регистра)
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


# Класс Sedan, наследующий от Vehicle
class Sedan(Vehicle):
    # Атрибут класса: ограничение на количество пассажиров
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


# Создаем объект класса Sedan
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Пытаемся изменить цвет на недопустимый
vehicle1.set_color('Pink')

# Изменяем цвет на допустимый
vehicle1.set_color('BLACK')

# Меняем владельца
vehicle1.owner = 'Vasyok'

# Проверяем, что изменилось
vehicle1.print_info()