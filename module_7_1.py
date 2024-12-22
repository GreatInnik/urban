class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self. category = category

    def __str__(self):
        return f"Наименование товара - {self.name}, Вес товара - {self.weight}, Категория товара - {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

    def add(self, *products):
        existing_products = {line.split(',')[0] for line in self.get_products()}
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in existing_products:
                    file.write(f"{product.name},{product.weight},{product.category}\n")
                    existing_products.add(product.name)
                else:
                    print(f"Продукт {product.name} уже есть в магазине")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())