class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retLis = []
        l_max = bin(2**len(nums))
        l_max = len(l_max[2:]) - 1
        
        for k in range(2**len(nums)):
            val = bin(k)
            val = val[2:]
            val = '0' * (l_max - len(val)) + val
            temp = []
            for x,y in enumerate(val):
                if y == '1':
                    temp.append(nums[x])
            temp = sorted(temp)
            if temp not in retLis:
                retLis.append(temp)
        return sorted(retLis)