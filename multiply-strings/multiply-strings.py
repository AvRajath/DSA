class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        val1 = 0
        val2 = 0
        k = 1
        for i in num1:
            temp = k*int(i)
            val1 = val1 + temp
            k*=10
        
        k = 1
        for j in num2:
            temp = k*int(j)
            val2 = val2 + temp
            k*=10
        
        return str(val1*val2)
        if val1>val2:
            retVal = 0
            while (val2>0):
                retVal = retVal + val1
                val2 = val2 - 1
            return str(retVal)
        else:
            retVal = 0
            while (val1>0):
                retVal = retVal + val2
                val1 -= 1
            return str(retVal)