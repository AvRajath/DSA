class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr = prices[0]
        m = 0
        for k in prices:
            if k - curr < 0:
                curr = k
            if k - curr > m:
                m = k - curr
        
        return m