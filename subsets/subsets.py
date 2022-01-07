class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        out = []
        for k in range(2**l):
            m = bin(k)
            m = m[2:]
            m = m[::-1]
            lis = []
            for x,y in enumerate(m):
                z = len(nums) - x - 1 
                if m[x] == '1':
                    lis.append(nums[z])
            out.append(lis)
        return out