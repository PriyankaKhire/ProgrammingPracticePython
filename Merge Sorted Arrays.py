# Merge Sorted Arrays
# https://leetcode.com/problems/merge-sorted-array/description
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # The strategy is to start from the back.
        # The ptr keeps track of nums1 from the back.
        ptr = m+n-1
        # Since our index start from 0, I have made n-1 and m-1
        while (ptr >= 0 and n-1 >= 0 and m-1 >= 0):
            # determine which number is greater
            if (nums1[m-1] > nums2[n-1]):
                nums1[ptr] = nums1[m-1]
                m -= 1
            else:
                nums1[ptr] = nums2[n-1]
                n -= 1
            ptr -= 1
        # copy the remaining numbers from nums2 into nums1
        while (n-1 >= 0):
            nums1[ptr] = nums2[n-1]
            ptr -= 1
            n -= 1
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """