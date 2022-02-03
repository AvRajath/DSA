class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        localMax = 0
        globalMax = -99999
        for k in nums:
            localMax = max(k, localMax+k)
            if localMax > globalMax:
                globalMax = localMax
        
        return globalMax
            
            