class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        i = 0
        j = 0
        dict = {}
        count = 0
        maxCount = count
        while i < len(s):
            if s[i] not in dict:
                dict[s[i]] = 1
                count += 1
                i+=1
                if maxCount < count:
                    maxCount = count
            else:
                count = 0
                dict = {}
                j +=1
                i = j
        return maxCount
        