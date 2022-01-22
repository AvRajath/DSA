class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        count = nums.count(0)
        print(count)
        swap = 0
        while swap != count:
            if nums[j] == 0:
                nums.pop(j)
                nums.append(0)
                swap +=1
            else:
                j += 1
        