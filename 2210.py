def countHillValley(nums):
    count=0
    prevv=nums[0]
    prev=nums[1]
    for i in range(2, len(nums)):
        print(prevv, prev, nums[i])
        if nums[i] != prev:
            if nums[i] > prev and prev > prevv:
                prevv = prev
                prev = nums[i]
            elif nums[i] < prev and prev < prevv:
                prevv = prev
                prev = nums[i]
            elif nums[i] < prev and prev > prevv:
                count += 1
                prevv = prev
                prev = nums[i]
            elif nums[i] > prev and prev < prevv:
                count += 1
                prevv = prev
                prev = nums[i]
            else:
                prevv = prev
                prev = nums[i]
        else:
            count += 0
        print(count)
    return count

def countHillValley0ms(nums):
    count=0
    prevv=nums[0]
    prev=nums[1]
    for i in range(2, len(nums)):
        if nums[i] != prev:
            if nums[i] < prev and prev > prevv:
                count += 1
            elif nums[i] > prev and prev < prevv:
                count += 1
            prevv = prev
            prev = nums[i]
    return count

#print(countHillValley([2,4,1,1,6,5]))
print(countHillValley([21,21,21,2,2,2,2,21,21,45]))