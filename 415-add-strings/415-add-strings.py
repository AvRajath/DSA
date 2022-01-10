class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = 0
        j = 0
        num2 = num2[::-1]
        num1 = num1[::-1]
        if len(num1) > len(num2):
            while len(num1) != len(num2):
                num2 += "0"
        else:
            while len(num1) != len(num2):
                num1 += "0"
            
        carry = 0
        s = 0
        ret = ""
        while i < len(num1) and j < len(num2):
            s = int(num1[i]) + int(num2[j]) + carry
            if s >= 10:
                s = s % 10
                carry = 1
            else:
                carry = 0
            ret += str(s)
            i += 1
            j += 1
        
        if carry:
            ret += "1"
        return ret[::-1]
                
            
            
        