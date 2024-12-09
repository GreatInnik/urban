class House:
    houses_history = []

    def __new__(cls, name, number_of_floors):
        instance = super(House, cls).__new__(cls)
        cls.houses_history.append(name)
        return instance

    def __del__(self):
        print (self.name, "снесён, но он останется в истории")
        if self.name in House.houses_history:
            House.houses_history.remove(self.name)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            return "Такого этажа не существует"
        else:
            return f"Вы на {new_floor} этаже"

h1 = House("ЖК Аврора", 30)
h2 = House("ЖК Ковчег", 24)

print(h1.name, h1.number_of_floors, "- этажное здание,", h1.go_to(3))
print(House.houses_history)

del h1
print(House.houses_history)