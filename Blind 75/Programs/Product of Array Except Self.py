# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
class Solution(object):
    def __init__(self):
        self.productLeftRight = []
        self.productRightLeft = []
    
    def getProductLeftToRight(self, nums):
        for n in nums:
            if not self.productLeftRight:
                self.productLeftRight.append(n)
            else:
                self.productLeftRight.append(self.productLeftRight[-1]*n)
    
    def getProductRightToLeft(self, nums):
        for n in reversed(nums):
            if not self.productRightLeft:
                self.productRightLeft.insert(0, n)
            else:
                self.productRightLeft.insert(0, self.productRightLeft[0]*n)
    
    def getProductExceptSelf(self, totalNums):
        answer = []
        for i in range(totalNums):
            if (i == 0):
                answer.append(self.productRightLeft[i+1])
            elif(i == totalNums-1):
                answer.append(self.productLeftRight[i-1])
            else:
                answer.append(self.productLeftRight[i-1]*self.productRightLeft[i+1])
        return answer
        
    def productExceptSelf(self, nums):
        self.getProductLeftToRight(nums)
        self.getProductRightToLeft(nums)
        return self.getProductExceptSelf(len(nums))
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
