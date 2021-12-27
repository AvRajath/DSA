class Solution(object):
    def subarraySum(self, nums, m):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        d[0] = 1
        s = 0
        count = 0
        for k in nums:
            s += k
            if s-m in d:
                count += d[s-m]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        return count
    