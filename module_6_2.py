class Vehicle:
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.colors = ["Red", "Blue", "Green", "Yellow", "Black", "White"]

    def get_model(self):
        return f"Модель: {self.__model}"

    def horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model(), self.horsepower(), self.get_color(), "Владелец:", self.owner)

    def set_color(self, new_color):
        if new_color not in self.colors:
            return f"Нельзя сменить цвет на {new_color}"
        else:
            self.__color = new_color
            return f"Транспорт был перекрашен в {new_color}"

class Sedan(Vehicle):
    def __init__(self, owner, model, engine_power, color, passengers_limit):
        super().__init__(owner, model, engine_power, color)
        self.__PASSENGERS_LIMIT = passengers_limit

vehicle = Vehicle("Виктор", "HR232", 11, "Blue")
sedan = Sedan("Алексей", "HR233", 12, "Red", 5)

vehicle.print_info()
print(vehicle.set_color("Red"))
sedan.print_info()