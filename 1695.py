def maximumUniqueSubarray(nums):
    unique_arr = []
    start = 0
    end = 0
    prev_mx = 0
    mx = 0
    for i in range(len(nums)):
        if not (nums[i] in unique_arr):
            end = i
            unique_arr.append(nums[i])
            mx += nums[i]
            print(start ,end)
        else:
            end = i
            unique_arr.append(nums[i])
            start += unique_arr.index(nums[i]) + 1
            del unique_arr[0: unique_arr.index(nums[i]) + 1]
            mx = sum(unique_arr)
            print(start ,end)
        if mx > prev_mx:
            prev_mx = mx
    return prev_mx

def maximumUniqueSubarray120ms(nums):
    max_sum = 0
    current_sum = 0
    num_set = set()
    start = 0

    for num in nums:
        if num in num_set:
            while nums[start] != num:
                current_sum -= nums[start]
                num_set.remove(nums[start])
                start += 1            
            
            start += 1
        else:
            num_set.add(num)
            current_sum += num                    
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum
                
# print(maximumUniqueSubarray([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]))
print(maximumUniqueSubarray([1,3,4,2,4,5,6]))
print(maximumUniqueSubarray([1,2,3,4,5,6,7,8,9,10]))
print(maximumUniqueSubarray([10,10,10,10,10,10,10,10,10,10]))