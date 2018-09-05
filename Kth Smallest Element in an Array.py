#Kth Smallest Element in an Array
#https://leetcode.com/problems/kth-largest-element-in-an-array/description/
class Solution(object):
    #returns the pos of pivot
    def partition(self, low, high, nums):
        pivot = low
        for i in range(low+1, high):
            if(nums[i] < nums[pivot]):
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot = i
        return pivot
    
    def findKthLargest(self, nums, k):
        low = 0
        high = len(nums)
        pivot = self.partition(low, high, nums)
        while(k != pivot):
            if(k > pivot):
                #go right
                low = pivot+1
            else:
                high = pivot-1
            pivot = self.partition(low, high, nums)
        print nums[pivot]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
#Main
o = Solution()
o.findKthLargest([3,2,1,5,6,4], 5)
