import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Масив для сортування
arr = [7, 2, 1, 6, 8, 5, 3]
frames = []

def record_frame(array, color_array):
    frames.append((array.copy(), color_array.copy()))

def quick_sort_visual(arr, low, high, color_array):
    if low >= high:
        return

    i, j = low, high
    pivot = arr[(low + high) // 2]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            color_array[i], color_array[j] = 'red', 'red'
            record_frame(arr, color_array)
            color_array[i], color_array[j] = 'blue', 'blue'
            i += 1
            j -= 1

    if low < j:
        quick_sort_visual(arr, low, j, color_array)
    if i < high:
        quick_sort_visual(arr, i, high, color_array)

def animate_sort(frames):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(frames[0][0])), frames[0][0], color=frames[0][1])
    ax.set_ylim(0, max(frames[0][0]) + 1)
    ax.set_title("Візуалізація QuickSort")

    def update(frame):
        values, colors = frame
        for rect, h, c in zip(bar_rects, values, colors):
            rect.set_height(h)
            rect.set_color(c)
        return bar_rects

    anim = animation.FuncAnimation(fig, update, frames=frames, blit=False, interval=700, repeat=False)
    plt.show()

# Початкові кольори (усі сині)
color_array = ['blue'] * len(arr)
record_frame(arr, color_array)

quick_sort_visual(arr, 0, len(arr) - 1, color_array)

animate_sort(frames)
