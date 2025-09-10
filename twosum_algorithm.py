import time
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_test_data(n):
    """Generate n distinct random integers"""
    # Create a set to ensure distinct values
    data = set()
    while len(data) < n:
        # Generate random integers in range [-n*10, n*10]
        val = random.randint(-n*10, n*10)
        data.add(val)
    return list(data)

def time_two_sum(n):
    """Time the two_sum function for input size n"""
    data = generate_test_data(n)
    
    start_time = time.perf_counter()
    count = two_sum(data)
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    return elapsed_time



def two_sum(arr):
    """
    Count pairs that sum to exactly 0
    """
    count = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == 0:
                count += 1
    
    return count


def run_experiments():
    """Run experiments for different input sizes"""
    sizes = [1000, 2000, 4000, 8000, 16000]
    times = []
    
    print(f"{'N':>10}{'Time (seconds)':>20}")
    print("-" * 30)
    
    for n in sizes:
        # Run multiple trials and take average
        trial_times = []
        for _ in range(3):  # 3 trials per size
            trial_time = time_two_sum(n)
            trial_times.append(trial_time)
        
        avg_time = sum(trial_times) / len(trial_times)
        times.append(avg_time)
        print(f"{n:10}{avg_time:20.4f}")
    
    return sizes, times

# Run the experiments
sizes, times = run_experiments()


# Create standard plot
fig, ax1 = plt.subplots(figsize=(10, 10))

# Standard scale plot
ax1.plot(sizes, times, 'bo-', linewidth=2, markersize=8)
ax1.set_xlabel('Input Size (N)', fontsize=12)
ax1.set_ylabel('Time (seconds)', fontsize=12)
ax1.set_title('2Sum Algorithm Performance', fontsize=14)
ax1.grid(True, alpha=0.3)

# Add annotations
for i, (x, y) in enumerate(zip(sizes, times)):
    ax1.annotate(f'({x}, {y:.2f})', 
                xy=(x, y), 
                xytext=(5, 5),
                textcoords='offset points',
                fontsize=9)

plt.show()


