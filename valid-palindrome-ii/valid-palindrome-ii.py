class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0
        high = len(s)-1
        if s == "":
            return True
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            elif s[low] !=s[high] : 
                if s[low+1:high+1] == s[low+1:high+1][::-1] or s[low:high] == s[low:high][::-1]:
                    return True
                else:
                    return False
        return True