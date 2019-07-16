#Product of Array Except Self
#https://leetcode.com/problems/product-of-array-except-self/
class Solution(object):
    def productExceptSelf(self, nums):
        leftToRight = [nums[0]]
        #To get product from left to right 
        for i in range(1, len(nums)):
            leftToRight.append(nums[i]*leftToRight[i-1])
        rightToLeft = [nums[-1]]
        #To get product from right to left
        for i in range(len(nums)-2, -1, -1):
            rightToLeft.insert(0, nums[i]*rightToLeft[0])
        #product except self is
        productList = [1 for i in range(len(nums))]
        for i in range(1, len(nums)-1):
            productList[i] = leftToRight[i-1] * rightToLeft[i+1]
        #print add to 0th and last position of product list
        productList[0] = rightToLeft[1]
        productList[-1] = leftToRight[-2]
        print productList
        """
        :type nums: List[int]
        :rtype: List[int]
        """
#Main
obj = Solution()
obj.productExceptSelf([1,2,3,4])
