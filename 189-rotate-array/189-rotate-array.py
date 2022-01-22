class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #nums = nums[::-1]
        #nums = rotateRest(nums, k)
        if len(nums) == 1:
            return
        
        k %= len(nums)
        rotateRest(nums, 0, len(nums)-1)
        rotateRest(nums, 0, k-1)
        rotateRest(nums, k, len(nums) - 1)
        

def rotateRest(arr, k, i):
    while k < i:
        arr[k], arr[i] = arr[i], arr[k]
        k += 1
        i -= 1
    
        