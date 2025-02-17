"""
Brian Gutt

Project 1: Program Performance Measurement


"""

import time
import random
import matplotlib.pyplot as plt

# Sorting Algorithms
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Function to generate random lists
def generate_random(size):
    return [random.randint(0, 104) for _ in range(size)]

# Function to measure execution time
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())  # Use a copy to avoid modifying the original list
    end_time = time.time()
    return end_time - start_time

# Test cases
input_sizes = [10, 100, 1000, 10000, 100000]
sorting_algorithms = {
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Bubble Sort": bubble_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
}

# Store results
results = {alg: [] for alg in sorting_algorithms}

# Run tests
for size in input_sizes:
    random_list = generate_random(size)
    for alg_name, alg_func in sorting_algorithms.items():
        time_taken = measure_time(alg_func, random_list)
        results[alg_name].append(time_taken)
        print(f"{alg_name} with {size} elements took {time_taken:.6f} seconds")

# Plotting the results
plt.figure(figsize=(10, 6))
for alg_name, times in results.items():
    plt.plot(input_sizes, times, label=alg_name)

plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Sorting Algorithm Performance")
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.show()