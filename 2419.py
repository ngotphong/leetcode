def longestSubarray(nums):
    if not nums:
        return 0
    
    max_val = nums[0]
    max_length = 1
    current_length = 1
    
    for i in range(1, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
            max_length = 1
            current_length = 1
        elif nums[i] == max_val:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 0
    
    return max_length

print(longestSubarray([1,2,3,3,2,2]))
print(longestSubarray([1,2,3,4]))
print(longestSubarray([100,5,5]))
