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

# Размеры списков
sizes = [10, 100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

# Перебираем каждый размер
for size in sizes:
    # Создаем список случайных чисел
    random_list = [random.randint(0, 1000000) for _ in range(size)]
    
    # Засекаем время сортировки
    start_time = time.time()
    sorted_list = merge_sort(random_list)
    elapsed_time = time.time() - start_time
    
    print(f"Время, затраченное на сортировку {size}: {elapsed_time:.2f} секунд")
