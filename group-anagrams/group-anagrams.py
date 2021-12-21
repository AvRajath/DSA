class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        d1 = {}
        mainList = []
        l = [0] * len(strs)
        for i, k in enumerate(strs):
            d1 = self.createDict(k)
            d2 = {}
            wordList = []
            if l[i] == 0:
                wordList.append(k)
                l[i] = 1
                for j in range(i+1, len(strs)):
                    d2 = self.createDict(strs[j])
                    if d1 == d2:
                        wordList.append(strs[j])
                        l[j] = 1
                mainList.append(wordList)
        return mainList
        
    def createDict(self, s):
        d = {}
        for k in s:
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
        return d """
        d = {}
        for k in strs:
            s = sorted(k)
            s = "".join(s)
            if s in d:
                d[s].append(k)
            else:
                d[s] = [k]
        return d.values()