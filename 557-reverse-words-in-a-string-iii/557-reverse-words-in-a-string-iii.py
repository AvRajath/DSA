class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = s.split(" ")
        for j,k in enumerate(sl):
            sl[j] = str(k)[::-1]
            
        return " ".join(sl)