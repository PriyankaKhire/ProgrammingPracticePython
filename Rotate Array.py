# Rotate Array
# https://leetcode.com/problems/rotate-array/description

class Solution(object):
    def rotate(self, nums, k):
        if (len(nums) == 1):
            return 
        # if k is greater than length of array then we just have to reverse numbers that are k mod length of array to get remainder
        if (k > len(nums)):
            k = k%len(nums)
        kList = []
        # remove the last k elements into the k list
        for i in range(len(nums)-k, len(nums)):
            kList.append(nums[i])
            nums[i] = "_"
        # move the numbers to the back
        ptr = len(nums) - k - 1 
        emptySpace = len(nums)-1
        while (ptr >= 0):
            # replace empty space with ptr number
            nums[emptySpace] = nums[ptr]
            emptySpace -= 1
            ptr -= 1
        # put the k list numbers into the nums list
        for i in range(k-1, -1, -1):
            nums[i] = kList.pop()
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
