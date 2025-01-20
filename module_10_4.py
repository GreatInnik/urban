import queue
import threading
from random import randint
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name, table):
        super().__init__()
        self.name = name
        self.table = table

    def run(self):
        sleep(randint(3, 10))
        print(f'{self.name} покушал(-а) и ушёл(ушла)')
        if self.table:
            self.table.guest = None


class StopSignal:
    """Класс-сигнал для остановки обработки очереди."""
    pass


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            self.queue.put(guest)
            print(f'{guest.name} в очереди')

        self.queue.put(StopSignal())

        for table in self.tables:
            if table.guest is None and not self.queue.empty():
                table.guest = self.queue.get()
                print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                table.guest.start()

    def discuss_guests(self):
        while True:
            guest = self.queue.get()
            if isinstance(guest, StopSignal):
                break

            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

            print(f'В очереди осталось {self.queue.qsize()} гостей.')
            sleep(1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name, None) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()


sleep(5)
print("Все гости обслужены, программа завершена.")