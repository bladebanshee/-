import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Размеры списков
sizes = [10, 100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

# Перебираем каждый размер
for size in sizes:
    # Создаем список случайных чисел
    random_list = [random.randint(0, 1000000) for _ in range(size)]
    
    # Засекаем время отсортировки
    start_time = time.time()
    selection_sort(random_list)
    elapsed_time = time.time() - start_time
    
    print(f"Время, затраченное на сортировку {size}: {elapsed_time:.2f} секунд")
