import time
import random 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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
    runtimes1 = []
    for i in range(5):
        total1 += time_algorithm(selection_sort, arr1)
        runtimes1.append(time_algorithm(selection_sort, arr1))
    print('Selection Sort Runtimes: ' + str(runtimes1))
    average1 = total1 / 5
    xpoints1 = [0, (len(arr1)-1)]
    ypoints1 = [0, total1]
    plt.plot(xpoints1, ypoints1, label = "Selection Sort", color = 'pink')

    arr2 = merge_sort(arr)
    total2 = 0
    runtimes2 = []
    for i in range(5):
        total2 += time_algorithm(merge_sort, arr2)
        runtimes2.append(time_algorithm(merge_sort, arr2))
    print('Merge Sort Runtimes: ' + str(runtimes2))
    average2 = total2 / 5
    xpoints2 = [0, (len(arr1)-1)]
    ypoints2 = [0, total2]
    plt.plot(xpoints2, ypoints2, label = "Merge Sort", color = 'green')

    plt.ylabel('Average Time')
    plt.xlabel('n')
    plt.title('Linear Graph of Avg. Time vs. n')

    plt.legend()
    plt.show()


def logarithm_plot(arr):
    arr1 = selection_sort(arr)
    total1 = 0
    runtimes1 = []
    for i in range(5):
        total1 += time_algorithm(selection_sort, arr1)
        runtimes1.append(time_algorithm(selection_sort, arr1))
    print('Selection Sort Runtimes: ' + str(runtimes1))
    average1 = total1 / 5
    xpoints1 = [0, (len(arr1)-1)]
    ypoints1 = [0, total1]
    plt.plot(xpoints1, ypoints1, label = "Selection Sort", color = 'pink')

    arr2 = merge_sort(arr)
    total2 = 0
    runtimes2 = []
    for i in range(5):
        total2 += time_algorithm(merge_sort, arr2)
        runtimes2.append(time_algorithm(merge_sort, arr2))
    print('Merge Sort Runtimes: ' + str(runtimes2))
    average2 = total2 / 5
    xpoints2 = [0, (len(arr1)-1)]
    ypoints2 = [0, total2]
    plt.plot(xpoints2, ypoints2, label = "Merge Sort", color = 'green')
    
    plt.ylabel('Average Time (log scale)')
    plt.xlabel('n')
    plt.title('Logarithmic Graph of Avg. Time vs. n')

    plt.semilogy(xpoints1, ypoints1)
    plt.semilogy(xpoints2, ypoints2)

    plt.legend()
    plt.show()

def table(n):
    median = 0
    selection = []

    print("Selection Sort Table")
    for i in range(len(n)):
        for j in range(5):
            random_array = random.sample(range(1,(n[i]+1)), n[i])
            median += time_algorithm(selection_sort, random_array)
        selection.append({n[i]: median})
    
    s = pd.DataFrame(selection)
    print(s)
    

    median = 0
    merge = []

    print("Merge Sort Table")
    for i in range(len(n)):
        for j in range(5):
            random_array = random.sample(range(1,(n[i]+1)), n[i])
            median += time_algorithm(merge_sort, random_array)
        merge.append({n[i]: median})
    
    m = pd.DataFrame(merge)
    print(m)




if __name__ == "__main__":
    random.seed(42)
    n = [100, 500, 1000, 5000]
    random_array = random.sample(range(1,(n[3]+1)), n[3])

    table(n)
    linear_plot(random_array)
    logarithm_plot(random_array)