#Pascal's Triangle II
#https://leetcode.com/problems/pascals-triangle-ii/
class Solution(object):
    def logic(self, rowIndex, output):
        if(rowIndex == 0):
            return output
        currentRow = [1]
        for i in range(len(output)-1):
            currentRow.append(output[i]+output[i+1])
        currentRow.append(1)
        return self.logic(rowIndex-1, currentRow)
        
    def getRow(self, rowIndex):
        if(rowIndex == 0):
            return [1]
        if(rowIndex == 1):
            return [1,1]
        print self.logic(rowIndex - 1, [1,1])
        """
        :type rowIndex: int
        :rtype: List[int]
        """

#Main
obj = Solution()
obj.getRow(3)
