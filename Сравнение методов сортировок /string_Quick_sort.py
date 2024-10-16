import random
import time
import string

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

sizes = [10, 100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

for size in sizes:
    # Создание списка случайных строк заданного размера
    random_list = [generate_random_string(random.randint(5, 15)) for _ in range(size)]
    
    start_time = time.time()  # Начало отсчета времени
    sorted_list = quick_sort(random_list)
    end_time = time.time()  # Конец отсчета времени
    
    # Вывод размера списка и времени сортировки
    print(f"Размер списка: {size}; Время, затраченное на сортировку: {end_time - start_time:.6f} секунд")
