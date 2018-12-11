#Best Time to Buy and Sell Stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution(object):
    def __init__(self, array):
        self.array = array
        self.matrix = [[0 for col in range(len(array))] for row in range(len(array))]
        self.maxProfit = 0
        self.maxProfitRow = None
        self.maxProfitCol = None

    def displayMatrix(self):
        for row in range(len(self.array)):
            print self.matrix[row]

    def fillMatrix(self):
        for row in range(len(self.array)):
            for col in range(row, len(self.array)):
                if(row == col):
                    self.matrix[row][col] = 0
                else:
                    self.matrix[row][col] = self.array[col] - self.array[row]
                    #find the max profit
                    if(self.maxProfit < self.matrix[row][col]):
                        self.maxProfit = self.matrix[row][col]
                        self.maxProfitRow = row
                        self.maxProfitCol = col

    def logic(self):
        self.fillMatrix()
        self.displayMatrix()
        print "The max profit can be obtained by buying stock on day ", self.maxProfitRow, " and selling on day ", self.maxProfitCol
        print "The max profit is ", self.maxProfit

#Main
obj1 = Solution([7,1,5,3,6,4])
obj1.logic()

obj2 = Solution([7,6,4,3,1])
obj2.logic()

obj3 = Solution([100, 180, 260, 310, 40, 535, 695])
obj3.logic()
