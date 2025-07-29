from functools import reduce

def smallestSubarrays(nums):
    target = reduce(lambda x, y: x | y, nums)
    lens = []
    for i in range(len(nums)):
        current_or = 0
        result = []
        j = i
        while current_or != target and j < len(nums):
            if nums[j] | current_or != current_or or len(nums) > j + 2 :
                result.append(nums[j])
            current_or |= nums[j]
            j += 1
        lens.append(len(result))
    return lens

def smallestSubarrays2(nums):
    n = len(nums)
    answer = [1] * n
    last = [0] * 32

    for i in range(n - 1, -1, -1):
        for b in range(32):
            if nums[i] & (1 << b):
                last[b] = i
        max_len = 1
        for b in range(32):
            if last[b]:
                max_len = max(max_len, last[b] - i + 1)
        answer[i] = max_len
    return answer
        
print(smallestSubarrays2([1,0,2,1,3]))
print(smallestSubarrays2([4,0,5,6,3,2])) # [4,3,2,2,1,1]