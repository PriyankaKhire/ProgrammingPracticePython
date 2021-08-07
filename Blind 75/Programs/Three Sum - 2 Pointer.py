# 3Sum
# https://leetcode.com/problems/3sum/

class Solution(object):
    
    def addArrayToPairs(self, pairs, array):
        if (array not in pairs):
            pairs.append(array)
    
    def ifMoreThan3Zeros(self, nums):
        count = 0
        for n in nums:
            if(n == 0):
                count = count + 1
            if (count > 3):
                return True
        return False
    
    # if there are more than 3 zeros in input we can remove the excess zeros.
    def removeExtraZeros(self, nums):
        if not(self.ifMoreThan3Zeros(nums)):
            return nums
        newNums = []
        for element in nums:
            if (element != 0):
                newNums.append(element)
        # add 3 zeros since we removed all zeros
        return newNums+[0,0,0]
        
    def threeSum(self, nums):
        # this function is present to remove excess time taken with too many zeros case.
        nums = self.removeExtraZeros(nums)
        # the final answer is going to be stored in this array.
        pairs = []
        # Time taken to sort n(log n)
        sortedNums = sorted(nums)
        for currIndex in range(len(sortedNums)):
            left = 0
            right = len(sortedNums)-1
            while(left < right):
                # even though the continue statement is frowned upon, we use it here so the while loop gets excuted again in case there are less than 3 numbers in nums array.
                if (left == currIndex):
                    left = left + 1
                    continue
                if (right == currIndex):
                    right = right - 1
                    continue
                answer = sortedNums[left] + sortedNums[right] + sortedNums[currIndex]
                if (answer == 0):
                    self.addArrayToPairs(pairs, sorted([sortedNums[left], sortedNums[right], sortedNums[currIndex]]))
                    # this statement is important, we have to move 'a' pointer otherwise we can get stuck in an infinite loop.
                    right = right - 1
                if (answer < 0):
                    left = left + 1
                if (answer > 0):
                    right = right - 1
        return pairs
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
