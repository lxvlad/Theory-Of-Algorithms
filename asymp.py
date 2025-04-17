import matplotlib.pyplot as plt
import numpy as np

# Значення n (розмір вхідних даних)
n = np.logspace(1, 3, 100)  # від 10^1 до 10^3

# -------- Швидке сортування --------
# Асимптотичні функції для Quicksort
qs_worst = n ** 2                     # O(n^2)
qs_average = n * np.log2(n)          # O(n log n)
qs_best = n * np.log2(n)             # O(n log n)

plt.figure(figsize=(10, 6))
plt.plot(n, qs_worst, 'r', label=r'$O(n^2)$ (найгірший випадок)')
plt.plot(n, qs_average, 'b', label=r'$O(n \log n)$ (середній випадок)')
plt.plot(n, qs_best, 'g', label=r'$O(n \log n)$ (найкращий випадок)')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Розмір вхідних даних (n)')
plt.ylabel('Часова складність')
plt.title('Асимптотична складність швидкого сортування')
plt.grid(True, which="both", ls="--", lw=0.5)
plt.legend()
plt.tight_layout()
plt.show()

# -------- Сортування вставками --------
# Асимптотичні функції для Insertion Sort
ins_worst = n ** 2                   # O(n^2)
ins_average = n ** 2                 # O(n^2)
ins_best = n                         # O(n)

plt.figure(figsize=(10, 6))
plt.plot(n, ins_worst, 'r', label=r'$O(n^2)$ (найгірший випадок)')
plt.plot(n, ins_average, 'b', label=r'$O(n^2)$ (середній випадок)')
plt.plot(n, ins_best, 'g', label=r'$O(n)$ (найкращий випадок)')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Розмір вхідних даних (n)')
plt.ylabel('Часова складність')
plt.title('Асимптотична складність сортування вставками')
plt.grid(True, which="both", ls="--", lw=0.5)
plt.legend()
plt.tight_layout()
plt.show()
