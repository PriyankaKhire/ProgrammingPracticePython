#Product of Array Except Self
#https://leetcode.com/problems/product-of-array-except-self/
class ExtrsSpace(object):
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

class WithoutExtraSpace(object):
    def productExceptSelf(self, nums):
        #calculate product from left to right like we did previously
        output = [nums[0]]
        for i in range(1, len(nums)):
            output.append(nums[i]*output[i-1])
        #start tracing output array backwards
        tempSpace = 1
        for i in range(len(nums)-1, 0, -1):
            output[i] = output[i-1]*tempSpace
            tempSpace = tempSpace*nums[i]
        #Finally we haven't filled the first space, and tempSpace holds the value
        output[0] = tempSpace
        print output
#Main
obj = WithoutExtraSpace()
obj.productExceptSelf([1,2,3,4, 5])
