# Minimum Difference Between Largest and Smallest Value in Three Moves
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# Solution idea taken from https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/discuss/730567/JavaC%2B%2BPython-Straight-Forward

class Solution(object):
    
    def kill1Big2Small(self, array):
        array[len(array)-1] = array[len(array)-2]
        array[0] = array[1] = array[2]
    
    def kill2Big1Small(self, array):
        array[len(array)-1] = array[len(array)-2] = array[len(array)-3]
        array[0] = array[1]
    
    def kill3Smallest(self, array):
        array[0] = array[1] = array[2] = array[3]
    
    def kill3Biggest(self, array):
        array[len(array)-1] = array[len(array)-2] = array[len(array)-3] = array[len(array)-4]
        
    def minDifference(self, nums):
        # if nums length is less than or equal to 4
        # so in that case we replace all elements with 1 element and the answer is 0
        if (len(nums) <= 4):
            return 0
        # Sort the array and Kill 3 biggest elements
        threeBig = sorted(nums)
        self.kill3Biggest(threeBig)
        threeBigDifference =  max(threeBig) - min(threeBig)
        # Sort the array and kill 3 smallest elements
        threeSmall = sorted(nums)
        self.kill3Smallest(threeSmall)
        threeSmallDifference = max(threeSmall) - min(threeSmall)
        # Sort the array and kill 2 big and 1 small
        twoBigOneSmall = sorted(nums)
        self.kill2Big1Small(twoBigOneSmall)
        twoBigOneSmallDifference = max(twoBigOneSmall) - min(twoBigOneSmall)
        # Sort the array and kill 1 big and 2 small
        oneBigTwoSmall = sorted(nums)
        self.kill1Big2Small(oneBigTwoSmall)
        oneBigTwoSmallDifference  = max(oneBigTwoSmall) - min(oneBigTwoSmall)
        return min(threeBigDifference, threeSmallDifference, twoBigOneSmallDifference, oneBigTwoSmallDifference)
        """
        :type nums: List[int]
        :rtype: int
        """
        
