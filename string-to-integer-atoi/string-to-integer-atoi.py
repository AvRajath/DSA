class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        val = s[0]
        i = 1
        while val == " " and i < len(s):
            s = s[1:]
            val = s[0]
    
        if s[0] == "+" :
            sign = 1
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s = s[1:]
        else:
            sign = 1
            
        k = 0
        l = []
        while k < len(s) and s[k].isdigit():
            l.append(int(s[k]))
            k = k + 1
        l = l[::-1]
        m = 1
        val = 0
        for n in l:
            temp = m * n
            val += temp
            m *= 10
        if val*sign > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif val*sign < -pow(2, 31):
            return -pow(2, 31)
        return val*sign
        
        
            
        