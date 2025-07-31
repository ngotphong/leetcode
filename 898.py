def subarrayBitwiseORs(arr):
    """
    Find the number of distinct bitwise ORs of all non-empty subarrays.
    
    Approach: For each position, we track all possible OR values that can be achieved
    by subarrays ending at that position. We use a set to track all unique OR values.
    """
    result = set()  # Track all unique OR values
    current_or = set()  # OR values ending at current position
    
    for num in arr:
        # Create new OR values by combining current number with previous OR values
        new_or = set()
        new_or.add(num)  # Single element subarray
        
        # Combine with all previous OR values
        for prev_or in current_or:
            new_or.add(prev_or | num)
        
        # Add all new OR values to result
        result.update(new_or)
        
        # Update current_or for next iteration
        current_or = new_or
    
    return len(result)

# Test cases
test_cases = [
    [0],           # Expected: 1 (only 0)
    [1,1,2],       # Expected: 3 (1, 1|1=1, 2, 1|1|2=3)
    [1,2,4],       # Expected: 6 (1, 2, 4, 1|2=3, 1|2|4=7, 2|4=6)
    [1,1,1],       # Expected: 1 (only 1)
    [1,2,3],       # Expected: 6 (1, 2, 3, 1|2=3, 1|2|3=3, 2|3=3)
]

for i, arr in enumerate(test_cases):
    result = subarrayBitwiseORs(arr)
    print(f"Test case {i+1}: arr = {arr}")
    print(f"Result: {result}")
    print()

# More detailed explanation
def subarrayBitwiseORs_detailed(arr):
    """
    Detailed version showing the process step by step.
    """
    result = set()
    current_or = set()
    
    print(f"Array: {arr}")
    print("Step-by-step process:")
    
    for i, num in enumerate(arr):
        new_or = set()
        new_or.add(num)
        
        for prev_or in current_or:
            new_or.add(prev_or | num)
        
        result.update(new_or)
        current_or = new_or
        
        print(f"  Position {i} ({num}): {sorted(new_or)}")
        print(f"  Total unique ORs so far: {sorted(result)}")
    
    return len(result)

print("Detailed example:")
subarrayBitwiseORs_detailed([1, 2, 4])
