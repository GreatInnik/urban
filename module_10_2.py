import threading
import time
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        warrior = 100
        timer = 0
        while warrior:
            warrior -= self.power
            print(f'{self.name} сражается день(дня)..., осталось {warrior}')
            sleep(1)
            timer += 1
        return f"{self.name} одержал победу спустя {timer} дней(дня)!"


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()