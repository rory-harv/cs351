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