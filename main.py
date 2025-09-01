import time
import random 
import numpy as np
import matplotlib.pyplot as plt

def time_algorithm(algo, arr):
    start = time.time()
    algo(arr.copy())
    return time.time() - start

# Starter code
def selection_sort(arr):

    start_time = time.perf_counter()

    length = len(arr)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j

        (arr[i], arr[min_index]) = (arr[min_index], arr[i])

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return arr

def merge_sort(arr):

    start_time = time.perf_counter()

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right, start_time)

def merge(left, right, start_time):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print(elapsed_time)
    return result
    
  



if __name__ == "__main__":
    random.seed(42)
    n = [100, 500, 1000, 5000]
    random_array = np.random.randint(1, n[0], size = n[0])

    merge_sort(random_array)