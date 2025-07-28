from functools import reduce

def countMaxOrSubsets(nums):
    target = reduce(lambda x, y: x | y, nums)
    def backtrack(start, current_or, current_subset):
        if current_or == target:
            result.append(current_subset[:])
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_or | nums[i], current_subset)
            current_subset.pop()
    result = []
    backtrack(0, 0, [])
    return len(result)

print(countMaxOrSubsets([3,1]))
print(countMaxOrSubsets([2,2,2]))
print(countMaxOrSubsets([3,2,1,5]))