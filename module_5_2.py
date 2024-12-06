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


h1 = House("ЖК Аврора", 30)

print(h1.name, h1.number_of_floors, "- этажное здание,", h1.go_to(3))
print(len(h1))
print(str(h1))