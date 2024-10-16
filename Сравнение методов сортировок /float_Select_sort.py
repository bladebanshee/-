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

sizes = [10, 100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

# Перебираем каждый размер
for size in sizes:
    # Создание списка случайных чисел с плавающей точкой заданного размера
    random_list = [random.uniform(1.0, 1000000.0) for _ in range(size)]
    
    # Засекаем время сортировки
    start_time = time.time()
    selection_sort(random_list)
    elapsed_time = time.time() - start_time
    
    # Вывод размера списка и времени сортировки
    print(f"Размер списка: {size}; Время, затраченное на сортировку: {elapsed_time:.6f} секунд")
