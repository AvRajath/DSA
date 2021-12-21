class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums) - 1
        flag = False
        while l > 0:
            if nums[l] <= nums[l-1]:
                l -= 1
            else:
                flag = True
                break
        
        small = nums[l]
        swapIndex = l
        oldLen = len(nums)
        if flag:
            for k in range(len(nums) - l):
                if nums[l+k] < small and nums[l+k] > nums[l-1]:
                    swapIndex = l+k
                    small = nums[l+k]
            nums[l-1], nums[swapIndex] = nums[swapIndex], nums[l-1]
            nums[l:] = sorted(nums[l:])
        else:
            nums.sort()
        