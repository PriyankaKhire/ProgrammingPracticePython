#Pascal's Triangle
#https://leetcode.com/problems/pascals-triangle/
class Solution(object):
    def logic(self, numRows, output):
        if(numRows == 0):
            return
        topRow = output[-1]
        currentRow = [1]
        for i in range(len(topRow)-1):
            currentRow.append(topRow[i]+topRow[i+1])
        currentRow.append(1)
        output.append(currentRow)
        self.logic(numRows-1, output)
        
    def generate(self, numRows):
        if(numRows == 0):
            return []
        if(numRows == 1):
            return [[1]]
        if(numRows == 2):
            return [[1], [1,1]]
        output = [[1], [1,1]]
        self.logic(numRows-2, output)
        print output
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
#Main
obj = Solution()
obj.generate(5)
