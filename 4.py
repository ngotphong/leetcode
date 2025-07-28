def findMedianSortedArrays(self, nums1, nums2):
    def findMedian(nums):
        middle = (len(nums) + 1) / 2
        if middle % 1 == 0:
            return nums[int(middle - 1)]
        else: 
            return (nums[int(middle - 1.5)] + nums[int(middle - 0.5)]) / 2
    return findMedian(sorted(nums1 + nums2))