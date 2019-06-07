#House Robber
#https://leetcode.com/problems/house-robber/
class Backtracking(object):
    def recurrse(self, nums, index, answer, maxAmount):
        if(sum(maxAmount) < sum(answer)):
            maxAmount[0] = sum(answer)
        for i in range(index+2, len(nums)):
            self.recurrse(nums, i, answer+[nums[i]], maxAmount)

    def logic(self, nums):
        maxAmount = [0]
        for i in range(len(nums)):
            self.recurrse(nums, i, [nums[i]], maxAmount)
        print "The max ammount that can be robbed is ", maxAmount[0]
            
    def rob(self, nums):
        self.logic(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        
class DynamicPrograming(object):
    def __init__(self):
        self.matrix = None

    def displayMatrix(self):
        for row in range(len(self.matrix)):
            print self.matrix[row]

    def returnMax(self, a, b):
        return max(a, b)

    def fillMatrix(self, nums):
        maxAmount = 0
        row = 0
        col = 0
        while(row<len(nums)):
            if(row == col or row+1 == col):
                self.matrix[row][col] = nums[row]
            else:
                self.matrix[row][col] = nums[col] + max(self.matrix[row][col-2], self.matrix[row][col-3])
            maxAmount = self.returnMax(maxAmount, self.matrix[row][col])
            col = col + 1
            if(col == len(nums)):
                row = row + 1
                col = row
        return maxAmount
            
    def rob(self, nums):
        self.matrix = [[0 for col in range(len(nums))] for row in range(len(nums))]        
        print "The max ammount that can be robbed is ", self.fillMatrix(nums)
        self.displayMatrix()
        """
        :type nums: List[int]
        :rtype: int
        """
#Main
obj = Backtracking()
obj.rob([5,7,1,3,8,2])

obj2 = Backtracking()
obj2.rob([1,2,3,1])

obj3 = Backtracking()
obj3.rob([2,7,9,3,1])

obj11 = DynamicPrograming()
obj11.rob([5,7,1,3,8,2])

obj22 = DynamicPrograming()
obj22.rob([1,2,3,1])

obj33 = DynamicPrograming()
obj33.rob([2,7,9,3,1])

obj4 = Backtracking()
obj4.rob([6,3,10,8,2,10,3,5,10,5,3])

obj44 = DynamicPrograming()
obj44.rob([6,3,10,8,2,10,3,5,10,5,3])
