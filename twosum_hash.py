def twosum_hash_table(nums, target):
    """
    Hash table approach: One-pass solution
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}  # Hash table to store value -> index mapping
    lookups = 0
    
    for i, num in enumerate(nums):
        complement = target - num
        lookups += 1
        
        if complement in seen:
            return [seen[complement], i], lookups
        
        seen[num] = i
    
    return None, lookups

# Test the hash table solution
nums = [2, 7, 11, 15]
target = 9
result, lookups = twosum_hash_table(nums, target)
print(f"Result: {result}")
print(f"Hash lookups made: {lookups}")