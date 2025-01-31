# Базовый класс Animal
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

# Базовый класс Plant
class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

# Класс Mammal, наследующий от Animal
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс Predator, наследующий от Animal
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс Flower, наследующий от Plant
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False

# Класс Fruit, наследующий от Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверяем атрибуты и методы
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)