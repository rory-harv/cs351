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
    length = len(arr)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j

        (arr[i], arr[min_index]) = (arr[min_index], arr[i])

    return arr

def merge_sort(arr):

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
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

    return result

def plotting_linear(arr, n):
    xpoints = []
    i = 1
    for i in range(n):
        xpoints.append(i)
    
    runtimes = []

    for i in range(5):
        runtimes.append(time_algorithm(arr))
    
    sum = 0
    for i in range(len(runtimes)):
        sum += runtimes[i]
    average = sum / len(arr)

    ypoints = [0, average]

    plt.plot(xpoints, ypoints)
    plt.show()
    

    
    




if __name__ == "__main__":
    random.seed(42)
    n = [100, 500, 1000, 5000]
    random_array = np.random.randint(1, n[0], size = n[0])
    plotting_linear(random_array, len(random_array))
    