class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if not food.edible:
                self.alive = False
                return f"{self.name} съел {food.name} и отравился."
            else:
                self.fed = True
                return f"{self.name} съел {food.name}. и наелся"

class Predator(Mammal):
    def eat(self, food):
        result = super().eat(food)
        return result

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.alive)
print(a2.fed)
print(a1.eat(p1))
print(a2.eat(p2))
print(a1.alive)
print(a2.fed)