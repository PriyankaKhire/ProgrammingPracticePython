# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        # Convert nums to heap
        heapq._heapify_max(nums)
        print nums
        # Pop k elements
        for i in range(k):
            element = heapq.heappop(nums)
            heapq._heapify_max(nums)
        return element
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
