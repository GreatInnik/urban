class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            return "Такого этажа не существует"
        else:
            return f"Вы на {new_floor} этаже"

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

h1 = House("ЖК Аврора", 30)
h2 = House("ЖК Ковчег", 24)

print(h1.name, h1.number_of_floors, "- этажное здание,", h1.go_to(3))
print(len(h1))
print(str(h1))
print(h1 == h2, h1 < h2, h1 <= h2, h1 > h2, h1 >= h2, h1 != h2)

h3 = h1 + 5
print(h3.name, h3.number_of_floors)

h1 += 15
print(h1.name, h1.number_of_floors)

h4 = 10 + h2
print(h4.name, h4.number_of_floors)