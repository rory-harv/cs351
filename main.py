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

    if len(arr) <= 1:
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

    
    result.extend(left[i:])
    result.extend(right[j:])

    return result
    
  
def linear_plot(arr):
    arr1 = selection_sort(arr)
    total1 = 0
    for i in range(5):
        total1 += time_algorithm(selection_sort, arr1)
    average1 = total1 / 5
    xpoints1 = [0, (len(arr1)-1)]
    ypoints1 = [0, total1]
    plt.plot(xpoints1, ypoints1, label = "Selection Sort", color = 'pink', linestyle = '-')

    arr2 = merge_sort(arr)
    total2 = 0
    for i in range(5):
        total2 += time_algorithm(merge_sort, arr2)
    average2 = total2 / 5
    xpoints2 = [0, (len(arr1)-1)]
    ypoints2 = [0, total2]
    plt.plot(xpoints2, ypoints2, label = "Merge Sort", color = 'green', linestyle = '--')

    plt.show()




if __name__ == "__main__":
    random.seed(42)
    n = [100, 500, 1000, 5000]
    random_array = random.sample(range(1,(n[2]+1)), n[2])

    #print(selection_sort(random_array))
    linear_plot(random_array)