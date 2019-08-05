#Split Array Largest Sum
#https://leetcode.com/problems/split-array-largest-sum/
class Solution(object):
    def __init__(self):
        self.lowestSum = None
        
    def canWeSplitIntoMSubArraysWithLessOrEqualGivenSum(self, array, m, givenSum, output, index):
        if(index == len(array)):
            if(len(output) == m):
                return True
            return
        subArray = []
        for i in range(index, len(array)):
            subArray.append(array[i])
            if(sum(subArray) <= givenSum):
                output.append(subArray)
                if(self.canWeSplitIntoMSubArraysWithLessOrEqualGivenSum(array, m, givenSum, output, i+1)):
                    return True
                output.pop()

    def binarySearch(self, nums, m, low, high):
        if(low > high):
            return
        mid = (low+high)/2
        if(self.canWeSplitIntoMSubArraysWithLessOrEqualGivenSum(nums, m, mid, [], 0)):
            self.lowestSum = mid
            self.binarySearch(nums, m, low, mid-1)
        else:
            self.binarySearch(nums, m, mid+1, high)

    def splitArray(self, nums, m):
        self.binarySearch(nums, m, max(nums), sum(nums))
        print self.lowestSum
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        
#Main
array = [7,2,5,10,8]
obj = Solution()
obj.splitArray(array, 2)
