class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1_lis = [0] * 26
        for k in s1:
            s1_lis[ord(k) - ord('a')] += 1
            
        for j in range(len(s2) - len(s1) + 1):
            str1 = s2[j:j+len(s1)]
            if checkEq(str1, s1_lis):
                return True
        
        return False
            
    

def checkEq(str1, s1Lis):
    s2Lis = [0] * 26
    for k in str1:
        s2Lis[ord(k) - ord('a')] += 1
        
    for k in range(26):
        if s2Lis[k] != s1Lis[k]:
            return False
    return True
        
    