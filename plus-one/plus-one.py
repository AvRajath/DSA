class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lasIndex = len(digits)
        lasIndex = lasIndex - 1
        count = lasIndex
        while(count == lasIndex):
            if digits[lasIndex] == 9 and lasIndex != 0:
                digits[lasIndex] = 0
                count = count - 1
                lasIndex = lasIndex - 1
            elif lasIndex == 0 and digits[lasIndex] == 9:
                digits[lasIndex] = 0
                count = count - 1
                digits.insert(0,1)
            else:
                digits[lasIndex] = digits[lasIndex] + 1
                count = count - 1
        return digits