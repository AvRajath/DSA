class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h = {}
        for k in nums:
            if k not in h:
                h[k] = 1
            else:
                return True
        return False
        