#Maximum Product Subarray
#https://leetcode.com/problems/maximum-product-subarray/description/
class Solution(object):
    def __init__(self):
        self.matrix = []
        self.largestProduct = -999999999

    def displayMatrix(self):
        for row in range(len(self.matrix)):
            print self.matrix[row]

    def fillMatrix(self, nums):
        #fill matrix diagonally
        colStart = 0
        row = 0
        col = 0
        while(colStart < len(nums)):
            if(row == col):
                self.matrix[row][col] = nums[col]
            else:
                self.matrix[row][col] = nums[col] * self.matrix[row][col-1]
            #find max product
            if(self.largestProduct < self.matrix[row][col]):
                self.largestProduct = self.matrix[row][col]
            row = row+1
            col = col+1
            if(row == len(nums) or col == len(nums)):
                row = 0
                colStart = colStart+1
                col = colStart
    
    def maxProduct(self, nums):
        self.matrix = [[0 for col in range(len(nums))] for row in range(len(nums))]
        self.fillMatrix(nums)
        self.displayMatrix()
        print self.largestProduct
        """
        :type nums: List[int]
        :rtype: int
        """

#Main
obj = Solution()
obj.maxProduct([2,3,-2,4])
