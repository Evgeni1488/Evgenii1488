class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        products_dict = {}

        # Преобразуем существующие продукты в словарь для удобства поиска
        for line in existing_products:
            if line.strip():
                name, weight, category = line.strip().split(', ')
                key = (name, category)
                products_dict[key] = float(weight)

        # Обрабатываем новые продукты
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                key = (product.name, product.category)
                if key in products_dict:
                    # Если продукт уже есть, увеличиваем вес
                    products_dict[key] += product.weight
                    print(f"Продукт {product.name} уже был в магазине, его общий вес теперь равен {products_dict[key]}")
                else:
                    # Если продукта нет, добавляем его в файл
                    file.write(f"{product}\n")
                    products_dict[key] = product.weight

        # Перезаписываем файл с обновленными данными
        with open(self.__file_name, 'w', encoding='utf-8') as file:
            for (name, category), weight in products_dict.items():
                file.write(f"{name}, {weight}, {category}\n")


# Пример использования
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    s1.add(p1, p2, p3)

    print(s1.get_products())