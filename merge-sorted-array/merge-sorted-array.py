class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        
        i = j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i = i+1
            else:
                for k in range(m+n-1, i, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                i = i+1
                j = j+1
        if j < n:
            for k in range(n-1, j-1, -1):
                nums1[m+n-1] = nums2[k]
                m = m-1"""
        p1 = m - 1
        p2 = n - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1