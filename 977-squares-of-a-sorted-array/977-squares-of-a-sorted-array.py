class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        l = 0
        r = len(nums) -1 
        i = len(nums) -1 
        while l<=r:
            if abs(nums[l]) < abs(nums[r]):
                num = nums[r]
                r -= 1
            else:
                num = nums[l]
                l += 1
            res[i] = num*num
            i -= 1
        return res