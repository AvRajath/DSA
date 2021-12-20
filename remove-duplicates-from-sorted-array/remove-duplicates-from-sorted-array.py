class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        ind = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            else:
                nums[ind] = nums[i+1]
                count += 1
                ind += 1
        return count
                