class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        count = 1
        s = sentence.split(" ")
        vowels = ['a', 'e', 'i', 'o', 'u']
        for j, k in enumerate(s):
            letter = k[0].lower()
            if letter in vowels:
                s[j] = s[j] + 'ma' + ('a' * count)
            else:
                s[j] = k[1:] + k[0] + 'ma' + ('a' * count)
            count += 1
        return " ".join(s)
        