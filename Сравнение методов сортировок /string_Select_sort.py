import random
import time
import string

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

sizes = [10, 100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

for size in sizes:
    # Создание списка случайных строк заданного размера
    random_list = [generate_random_string(random.randint(5, 15)) for _ in range(size)]
    
    start_time = time.time()  # Начало отсчета времени
    selection_sort(random_list)
    end_time = time.time()  # Конец отсчета времени
    
    # Вывод размера списка и времени сортировки
    print(f"Размер списка: {size}; Время, затраченное на сортировку: {end_time - start_time:.6f} секунд")
