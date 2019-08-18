# Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def binarySearch(self, low, high):
        if(low > high):
            return
        mid = (low+high)/2
        currentGuess = guess(mid)
        if(currentGuess == 0):
            return mid
        if(currentGuess == -1):
            return self.binarySearch(low, mid-1)
        else:
            return self.binarySearch(mid+1, high)
        
    def guessNumber(self, n):
        return self.binarySearch(0, n)
        """
        :type n: int
        :rtype: int
        """
        
