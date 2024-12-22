class Animal:
    def __init__(self, speed = 0):
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0

        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += dx
        self._cords[1] += dy
        self._cords[2] += dz

        if self._cords[2] < 0:
            print("It's too deep, I can't dive :(")
            return self._cords[2]

    def get_cords(self):
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        return self.sound

class Bird(Animal):
    def __init__(self, speed = 0):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        return "Here are(is) 3 eggs for you"

class AquaticAnimal(Animal):
    def __init__(self, speed = 0):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= dz
        return abs(self._cords[2])

class PoisonousAnimal(Animal):
    def __init__(self, speed = 0):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed=0):
        super().__init__(speed)
        self.sound = "Click-click-click"


db = Duckbill(speed = 10)

print(db.live)
print(db.beak)

print(db.speak())
db.attack()

db.move(1, 2, 3)
print(db.get_cords())
db.dive_in(6)
print(db.get_cords())

print(db.lay_eggs())