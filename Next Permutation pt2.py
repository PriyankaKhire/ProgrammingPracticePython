# Next Permutation
# https://leetcode.com/problems/next-permutation/
class Solution(object):
    def __init__(self):
        self.allCombinations = []
        
    def isDescending(self, nums):
        for i in range(len(nums)-1):
            if (nums[i] < nums[i+1]):
                return False
        return True
    
    def getAllPermutations(self, nums, answer, visited):
        if (len(answer) == len(nums)):
            # convert list to int and append to array.
            self.allCombinations.append(int(''.join(str(e) for e in answer)))
            return
        for i in range(len(visited)):
            if (visited[i] == False):
                visited[i] = True
                self.getAllPermutations(nums, answer+[nums[i]], visited)
                visited[i] = False
    
    def findAllNumsLargerThanCurrNum(self, num, numberList):
        largeNums = []
        for currNum in numberList:
            if (currNum > num):
                largeNums.append(currNum)
        return largeNums
    
    def logic(self, nums):
        self.getAllPermutations(nums, [], [False for i in range(len(nums))])
        currentNumber = int(''.join(str(e) for e in nums))
        largeNums = self.findAllNumsLargerThanCurrNum(currentNumber, self.allCombinations)
        # get the smallest number from there
        nextSmallestNum = min(largeNums)
        # convert it into list
        return [int(n) for n in str(nextSmallestNum)]
    
    def nextPermutation(self, nums):
        if (self.isDescending(nums)):
            nums.sort()
            return
        print self.logic(nums)
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
