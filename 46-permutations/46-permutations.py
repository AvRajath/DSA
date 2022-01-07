class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute(n):
            if n == len(nums):
                out.append(nums[:])
            for i in range(n, len(nums)):
                nums[i], nums[n] = nums[n], nums[i]
                permute(n+1)
                nums[i], nums[n] = nums[n], nums[i]
            
        out = []
        permute(0)
        return out