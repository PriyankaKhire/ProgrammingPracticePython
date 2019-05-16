#Wiggle Sort
#https://leetcode.com/problems/wiggle-sort/
#https://leetcode.com/problems/wiggle-sort-ii/
class MediansOfMedians(object):
    def __init__(self, array):
        self.array = array
        self.medianIndex = len(array)/2
        
    def getMedians(self, array, index, medians):
        if(index >= len(array)):
            return medians
        if(index+5 < len(array)):
            chunk = array[index:index+5]
        else:
            chunk = array[index:len(array)]
        chunk.sort()
        medians.append(chunk[(len(chunk))/2])
        return self.getMedians(array, index+5, medians)

    def getPivot(self, medians):
        while(len(medians) != 1):
            medians = self.getMedians(medians, 0, [])
        return medians[0]

    def partition(self, pivot, array, low, high):
        if (low == high):
            return high, array
        while(low < high):
            while(low < high and array[low] <= pivot):
                low = low + 1
            while(low < high and array[high] > pivot):
                high = high - 1
            array[low], array[high] = array[high], array[low]
        #place pivot, high will be at pivot index
        low = 0            #$$ essentially we want these 2 steps to only take place if
        high = high - 1 #$$ and only if the low and high has gone through the above while loop
        while(low < high):
            while(low < high and array[low] != pivot):
                low = low + 1
            while(low < high and array[high] == pivot):
                high = high - 1
            array[low], array[high] = array[high], array[low]
        return high, array

    def logic(self):
        array = self.array
        pivotIndex = 0
        low = 0
        high = len(array)-1
        while(pivotIndex != self.medianIndex):
            pivot = self.getPivot(array[low:high+1])
            pivotIndex, array = self.partition(pivot, array, low, high)
            if(pivotIndex > self.medianIndex):
                high = pivotIndex-1
            else:
                low = pivotIndex+1
        return array, pivotIndex
        
class Solution(object):
    def wiggleSort(self, nums):
        o = MediansOfMedians(nums[0:len(nums)])
        partitionedArray, pivotIndex = o.logic()
        i = 0
        j = pivotIndex
        nums = []
        print partitionedArray
        while(i < len(partitionedArray)/2 or j<len(partitionedArray)):
            nums.append(partitionedArray[i])
            nums.append(partitionedArray[j])
            i = i+1
            j = j+1
        print nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

#Main
obj = Solution()
obj.wiggleSort([92, 56, 14, 38, 50, 44, 84, 67, 96, 20, 83, 39, 43, 85, 25, 91, 99])

obj = Solution()
obj.wiggleSort([1,5,1,1,6,4])
