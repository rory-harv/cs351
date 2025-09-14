import time
import random
import numpy as np
import matplotlib.pyplot as plt

def three_sum_brute_force(arr):
    """
    Count pairs that sum to target value
    """

    count = 0
    n = len(arr)
    comparisons = 0
    
    if n < 3:   # initial length evaluation
        return False

    for i in range(n-2):    # loop through without going out of bounds/double evaluating elements
        for j in range(i + 1, n):   # not double evaluating same first index
            for k in range(j + 1, n):   # not double evaluating same first index
                comparisons += 1
                if arr[i] + arr[j] + arr[k] == target:
                    count += 1
    
    return count, comparisons


def generate_test_data(n):
    """Generate n distinct random integers"""
    # Create a set to ensure distinct values
    data = set()
    while len(data) < n:
        # Generate random integers in range [-n*10, n*10]
        val = random.randint(-n*10, n*10)
        data.add(val)
    return list(data)

def time_three_sum(n):
    """Time the three_sum function for input size n"""
    data = generate_test_data(n)
    
    start_time = time.perf_counter()
    count, comps = three_sum_brute_force(data)
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    return elapsed_time, comps

def run_experiments():
    """Run experiments for different input sizes"""
    sizes = [50, 100, 200, 400, 800]
    times = []
    coms = []

    print(f"{'N':>10}{'Time (seconds)':>20}{'Comparisons':>20}")
    print("-" * 50)
    
    for n in sizes:
        # Run multiple trials and take average
        trial_times = []
        comparisons = []
        for _ in range(10):  # 10 trials per size
            trial_time, comps = time_three_sum(n)
            trial_times.append(trial_time)
            comparisons.append(comps)
        
        avg_time = sum(trial_times) / len(trial_times)
        times.append(avg_time)
        avg_comps = sum(comparisons) / len(comparisons)
        coms.append(avg_comps)
        print(f"{n:10}{avg_time:20.4f}{avg_comps:20}")
    
    return sizes, times, coms


def analyze_brute_force_iterations(n: int) -> None:
    """
    Detailed analysis of how many comparisons the brute force algorithm makes
    """
    print(f"Analyzing Brute Force for array of size {n}\n")
    print("Nested Loop Structure:")
    print("for i in range(n-2):          # Outer loop")
    print("    for j in range(i+1, n):  # Inner loop")
    print("        for k in range(j+1, n)   # Second inner loop")
    print("            compare(arr[i], arr[j], arr[k])")
    print("\n" + "="*60)
    
    # Show iterations for each value of i
    print("\nIterations breakdown:")
    print(f"{'i':<10} {'j ranges from':<20} {'k ranges from':<20} {'Comparisons':<15}")
    print("-"*65)
    
    total = 0
    iterations_per_i = []
    
    for i in range(n-1):
        j_start = i + 1
        j_end = n - 1
        k_start = j_start + 1
        k_end = n 
        count = n - (i + 1)
        iterations_per_i.append(count)
        total += count
        
        if i < 5 or i == n-2:  # Show first few and last
            if j_start <= j_end:
                if k_start <= k_end:
                    print(f"{i:<10} {f'{j_start} to {j_end}':<20} {f'{k_start} to {k_end}':<20} {count:<15}")
                else:
                    print(f"{i:<10} {f'{j_start} to {j_end}':<20} {'(none)':<20} {count:<15}")
            else:
                if k_start <= k_end:
                    print(f"{i:<10} {'(none)':<20} {f'{k_start} to {k_end}':<20} {count:<15}")
                else:
                    print(f"{i:<10} {'(none)':<20} {'(none)':<20} {count:<15}")

        elif i == 5:
            print(f"{'...':<10} {'...':<20} {'...':<20} {'...':<15}")
    
    print("-"*65)
    print(f"{'TOTAL':<10} {'':<20} {'':<20} {total:<15}")
    
    # Show the arithmetic series
    print("\n" + "="*60)
    print("This forms an arithmetic series:")
    series_str = " + ".join(str(x) for x in iterations_per_i[:min(5, n)])
    if n > 5:
        series_str += " + ... + " + str(iterations_per_i[-1])
    print(f"Total = {series_str}")
    print(f"Total = (n-1) + (n-2) + (n-3) + ... + 2 + 1")
    
    # Derive the formula
    print("\nMathematical Derivation:")
    print("-"*40)
    print("Let S = (n-1) + (n-2) + ... + 2 + 1")
    print("This is the sum of first (n-1) natural numbers")
    print("\nUsing the arithmetic series formula:")
    print("Sum of 1 to k = k(k+1)/2")
    print(f"\nTherefore: S = (n-1)((n-1)+1)/2")
    print(f"           S = (n-1)(n)/2")
    print(f"           S = {(n-1)*n//2}")
    
    # Verify
    calculated = (n-1) * n // 2
    print(f"\nVerification: {total} = {calculated} ✓")




if __name__ == "__main__":
    target = 0
    # Test the brute force solution
    test_arrays = [
    [1, -1, 2, -2, 3],
    [0, 0, 0],
    [5, -5, 10, -10, 5, -5],
    [1, 2, 3, 4, 5],
    [0, 0, 0, 0]
    ]

    # for arr in test_arrays:
    #     result, comps = three_sum_brute_force(arr)
    #     print(f"Array: {arr}")
    #     print(f"  Target-sum pairs: {result}")
    #     print(f"  Comparisons made: {comps}")
    #     print()


    # Run the experiments
    sizes, times, coms = run_experiments()

    # Demonstrate with different sizes
    for i in range(len(sizes)):
        analyze_brute_force_iterations(sizes[i])