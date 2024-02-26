# Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution(object):
    def recurse(self, prevRow, currIndex, rowIndex):
        print prevRow
        if (currIndex == rowIndex):
            return prevRow
        currRow = []
        for i in range(len(prevRow) + 1):
            if (i == 0 or i == len(prevRow)):
                currRow.append(1)
                continue
            num = prevRow[i - 1] + prevRow[i]
            currRow.append(num)
        return self.recurse(currRow, currIndex + 1, rowIndex)

    def getRow(self, rowIndex):
        if (rowIndex == 0):
            return [1]
        if (rowIndex == 1):
            return [1, 1]
        # For row index >= 2
        row = [1, 1]
        return self.recurse(row, 2, rowIndex + 1)
        """
        :type rowIndex: int
        :rtype: List[int]
        """
