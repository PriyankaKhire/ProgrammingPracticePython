# Wiggle Sort II
# https://leetcode.com/problems/wiggle-sort-ii/

# uses O(nlogn) time and O(n) space 
class Solution1(object):
    def wiggleSort(self, nums):
        nums.sort()
        if(len(nums) == 1 or len(nums) == 2):
            return
        # sort array
        nums.sort()
        # split array into 2 halves
        firstHalf = nums[:len(nums)/2]
        secondHalf = nums[len(nums)/2:]
        nums = []
        for i in range(len(firstHalf)):
            # starting with second half first we alternately combine them.
            # swap first half of numbers with second half
            # for sorted array with indices: 0 1 2 3 4 5 6
            # we first split them in half
            # first half 0 1 2
            # second half 3 4 5 6
            # then combine them starting with second half first
            # 3 0 4 1 5 2 6
            nums.append(secondHalf[i])
            nums.append(firstHalf[i])
        print nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
# to further better this, we can use quick sort partition algorithem to first partition the array
# so the left half will contain elements less than median
# and right half will contain elements greater than median
class PartitionAlgo(object):
    
    def getPivotIndex(self, elements):
        return len(elements)/2
    
    def partition(self, elements):
        pivioIndex = self.getPivotIndex(elements)
        start = 0
        end = len(elements)-1
        print "Pivot",elements[pivioIndex]
        while(start < end):
            while(start < end and elements[start] <= elements[pivioIndex]):
                start = start+1
            while(start < end and elements[end] >= elements[pivioIndex]):
                end = end - 1
            print "Swapping",elements[start],elements[end]
            elements[start],elements[end] = elements[end], elements[start]
        # finally swap start with pivot index
        elements[start],elements[pivioIndex] = elements[pivioIndex], elements[start]
        print elements

# Main
p = PartitionAlgo()
p.partition([4,2,6,3,5,1,7])

# to make the above algo even better use select algo, to get pivot index
# where you first partition elements in group of 5
# sort these 5 using selection sort
# get their medians
# then sort the medians
# then get median of medians
# and thats your pivot.
        
