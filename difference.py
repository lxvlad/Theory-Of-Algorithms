import time
import random

# --------- Алгоритми ---------
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --------- Вимірювання часу ---------
def measure_time(sort_function, array):
    start = time.perf_counter()
    sort_function(array.copy())
    end = time.perf_counter()
    return end - start

# --------- Розміри масивів ---------
sizes = [500, 5000]

# --------- Порівняння ---------
for size in sizes:
    print(f"\n--- Розмір масиву: {size} елементів ---")

    best_case = list(range(size))
    worst_case = list(range(size, 0, -1))
    average_case = best_case.copy()
    random.shuffle(average_case)

    cases = {
        "Найкращий випадок": best_case,
        "Середній випадок": average_case,
        "Найгірший випадок": worst_case
    }

    for case_name, arr in cases.items():
        t_quick = measure_time(quicksort, arr)
        t_insert = measure_time(insertion_sort, arr)
        print(f"{case_name}:")
        print(f"  Швидке сортування: {t_quick:.4f} сек")
        print(f"  Сортування вставками: {t_insert:.4f} сек\n")
