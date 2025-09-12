
import random

def three_sum(arr):
    """
    Count pairs that sum to target value
    """

    count = 0
    n = len(arr)
    
    if n < 3:
        return False

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    count += 1
    
    return count

if __name__ == "__main__":
    target = 0
    n = [100, 500, 1000, 5000]
    random_array = random.sample(range(1,(n[3]+1)), n[3])