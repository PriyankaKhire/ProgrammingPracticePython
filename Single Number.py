#Single Number
#https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        xorValue = 0
        for num in nums:
            xorValue = xorValue ^ num
        print "The single number is ", xorValue
        """
        :type nums: List[int]
        :rtype: int
        """
#Main
obj = Solution()
obj.singleNumber([4,1,2,1,2])
print "Xor of 2 numbers is 0, we use this logic"
