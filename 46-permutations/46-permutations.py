class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retLis = []
        def perm(l):
            if l == len(nums):
                retLis.append(nums[:])
            
            for k in range(l, len(nums)):
                nums[l], nums[k] = nums[k], nums[l]
                perm(l+1)
                nums[l], nums[k] = nums[k], nums[l]
              
        perm(0)
        return retLis