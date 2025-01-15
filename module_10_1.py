import threading
import time
from time import sleep


def write_words(word_count, file_name, event):
    start_time = time.time()
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Завершилась запись в файл {file_name}")
    event.set()
    return duration


threads = []
events = []
durations = []


for args in [(10, "example1.txt"), (30, "example2.txt"), (200, "example3.txt"), (100, "example4.txt"),
             (10, "example5.txt"), (30, "example6.txt"), (200, "example7.txt"), (100, "example8.txt")]:

    event = threading.Event()
    events.append(event)

    thread = threading.Thread(target=lambda a=args, e=event: durations.append(write_words(*a, e)))
    threads.append(thread)
    thread.start()


    if len(threads) % 4 == 0:
        for e in events[-4:]:
            e.wait()

        total_duration = sum(durations[-4:])
        print(f"Работа потоков {time.strftime('%H:%M:%S', time.gmtime(total_duration))}")


for thread in threads:
    thread.join()