class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        newStr = ""
        stack = []
        removeIndex = set()
        for j,k in enumerate(s):
            if k == "(":
                stack.append(j)
            
            if k == ")":
                if len(stack) == 0:
                    removeIndex.add(j)
                else:
                    stack.pop()
        removeIndex = removeIndex.union(set(stack))
        newStr = ""
        for j, k in enumerate(s):
            if j not in removeIndex:
                newStr = newStr + k
        return newStr