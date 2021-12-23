class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 1
        left = [1]
        right = [1]
        idx = 0
        for k in range(len(nums) - 1):
            left.append(i * nums[k])
            i = i*nums[k]
    
        i = 1
        for k in range(len(nums) - 1, 0, -1):
            right.append(i * nums[k])
            i = i*nums[k]
        right.reverse()
        ret = []
        for k in range(len(right)):
            ret.append(left[k] * right[k])
        
        return ret