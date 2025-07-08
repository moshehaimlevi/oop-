import threading
import time
from concurrent.futures import ThreadPoolExecutor
import random
import string

################ STEP ONE ################
def print_sequence(name, count):
    for i in range(count):
        print(f"Thread {name}: i={i}")
        time.sleep(0.3)

thread1 = threading.Thread(target=print_sequence, args=("Alpha", 5))
thread2 = threading.Thread(target=print_sequence, args=("Beta", 3))
thread3 = threading.Thread(target=print_sequence, args=("Gamma", 4))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

################ STEP TWO ################
def print_sequence(name, count):
    for i in range(count):
        print(f"Thread {name}: i={i}")
        time.sleep(0.3)


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(print_sequence, "Alpha", 5)
    executor.submit(print_sequence, "Beta", 3)
    executor.submit(print_sequence, "Gamma", 4)

################ BONUS ################
def print_sequence(name, count):
    for i in range(count):
        print(f"Thread {name}: i={i}")
        time.sleep(0.3)


def random_name():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

tasks = [(random_name(), random.randint(2, 6)) for _ in range(random.randint(5, 10))]


with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(print_sequence, name, count) for name, count in tasks]


for future in futures:
    future.result()

print("All threads completed!")