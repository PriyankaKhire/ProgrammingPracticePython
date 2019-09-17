# Wiggle Sort
# https://leetcode.com/problems/wiggle-sort/
class Solution(object):
    def wiggleSort(self, nums):
        if(len(nums) == 1):
            return 
        if(len(nums) == 2):
            nums.sort()
            return 
        nums.sort()
        print nums
        i = 1
        while(i < len(nums)-1):
            # swap i with i+1
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i = i+2
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
# I did above method as suggested by leetcode solution, not proud of it.
# this is what I came up with
'''
1) if length of nums == even
    -> Sort numbers
    -> Take first half of numbers and reverse them
    -> starting with index 0 swap alterante until you reach mid
2) if length of nums == odd
    -> Sort numbers
    -> reverse numbers from index 0 to mid-1
    -> starting from index 0 swap alternate until you reach mid-1
'''
# Obviously the above still runs in O(nlogn) time but is a tad bit complicated.
