class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for k in s:
            d[k] = d.get(k, 0) + 1
        
        for k in t:
            d[k] = d.get(k, 0) - 1
        
        d = sorted(d.items(), key = lambda x: x[1])
        return d[0][0]