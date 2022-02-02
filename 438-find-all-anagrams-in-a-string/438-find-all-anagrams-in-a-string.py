class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        
        p_lis = Counter(p)
        s_lis = Counter()
        retLis = []
        for k in range(len(s)):
            s_lis[s[k]] += 1
            if k >= len(p):
                if s_lis[s[k - len(p)]] == 1:
                    del s_lis[s[k-len(p)]]
                else:
                    s_lis[s[k - len(p)]] -= 1
            if s_lis == p_lis:
                retLis.append(k - len(p) + 1)
                
        return retLis