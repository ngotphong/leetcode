def find_subsets_brute_force(arr, target):
    """Brute force approach - check all possible subsets"""
    from itertools import combinations
    
    result = []
    n = len(arr)
    
    # Check all possible combinations of different sizes
    for size in range(1, n + 1):
        for combo in combinations(arr, size):
            if sum(combo) == target:
                result.append(list(combo))
    
    return result

def find_subsets_backtracking(arr, target):
    """Backtracking approach - more efficient for larger arrays"""
    def backtrack(start, current_sum, current_subset):
        # If we've found a valid subset
        if current_sum == target:
            result.append(current_subset[:])
            return
        
        # Try adding each remaining element
        for i in range(start, len(arr)):
            # Skip duplicates to avoid duplicate subsets
            if i > start and arr[i] == arr[i-1]:
                continue
            
            # Add current element
            current_subset.append(arr[i])
            backtrack(i + 1, current_sum + arr[i], current_subset)
            current_subset.pop()  # Backtrack
    
    arr.sort()  # Sort to handle duplicates properly
    result = []
    backtrack(0, 0, [])
    return result

def find_subsets_dp(arr, target):
    """Dynamic programming approach - finds count of subsets"""
    n = len(arr)
    # dp[i][j] = number of ways to get sum j using first i elements
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    
    # Base case: empty subset has sum 0
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Don't include current element
            dp[i][j] = dp[i-1][j]
            # Include current element if possible
            if arr[i-1] <= j:
                dp[i][j] += dp[i-1][j - arr[i-1]]
    
    return dp[n][target]

def find_subsets_with_negative(arr, target):
    """Handle arrays with negative numbers"""
    def backtrack(start, current_sum, current_subset):
        if current_sum == target:
            result.append(current_subset[:])
        
        for i in range(start, len(arr)):
            current_subset.append(arr[i])
            backtrack(i + 1, current_sum + arr[i], current_subset)
            current_subset.pop()
    
    result = []
    backtrack(0, 0, [])
    return result

# Test the functions
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 7),
        ([1, 1, 2, 2, 3], 4),
        ([1, -1, 2, -2, 3], 0),
        ([1, 2, 3], 3)
    ]
    
    for arr, target in test_cases:
        print(f"\nArray: {arr}, Target: {target}")
        print("-" * 40)
        
        # Brute force
        print("Brute Force Results:")
        subsets_bf = find_subsets_brute_force(arr, target)
        for subset in subsets_bf:
            print(f"  {subset} = {sum(subset)}")
        
        # Backtracking
        print("Backtracking Results:")
        subsets_bt = find_subsets_backtracking(arr, target)
        for subset in subsets_bt:
            print(f"  {subset} = {sum(subset)}")
        
        # DP count
        count = find_subsets_dp(arr, target)
        print(f"Total number of subsets (DP): {count}")
        
        # With negative numbers
        if any(x < 0 for x in arr):
            print("With negative numbers:")
            subsets_neg = find_subsets_with_negative(arr, target)
            for subset in subsets_neg:
                print(f"  {subset} = {sum(subset)}")

# Performance comparison
def performance_test():
    import time
    import random
    
    # Generate test array
    arr = [random.randint(1, 20) for _ in range(15)]
    target = 50
    
    print(f"Performance test with array of length {len(arr)}")
    print(f"Target: {target}")
    
    # Test brute force
    start = time.time()
    result_bf = find_subsets_brute_force(arr, target)
    time_bf = time.time() - start
    
    # Test backtracking
    start = time.time()
    result_bt = find_subsets_backtracking(arr, target)
    time_bt = time.time() - start
    
    print(f"Brute force: {len(result_bf)} subsets in {time_bf:.4f}s")
    print(f"Backtracking: {len(result_bt)} subsets in {time_bt:.4f}s")

if __name__ == "__main__":
    performance_test() 