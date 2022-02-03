class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        no_of_ele = k
        d = {}
        for k in nums:
            d[k] = d.get(k, 0) + 1
            
        d = sorted(d.items(), key = lambda x: x[1], reverse = True)
        print(d)
        retLis = []
        for i in range(no_of_ele):
            retLis.append(d[i][0])
            
        return retLis