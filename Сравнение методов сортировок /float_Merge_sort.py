import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

sizes = [10, 100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

# Перебираем каждый размер
for size in sizes:
    # Создание списка случайных чисел с плавающей точкой заданного размера
    random_list = [random.uniform(1.0, 1000000.0) for _ in range(size)]
    
    # Засекаем время сортировки
    start_time = time.time()
    sorted_list = merge_sort(random_list)
    elapsed_time = time.time() - start_time
    
    # Вывод размера списка и времени сортировки
    print(f"Размер списка: {size}; Время, затраченное на сортировку: {elapsed_time:.6f} секунд")
