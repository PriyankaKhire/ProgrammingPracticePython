# Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/description/

class Solution(object):
    def generateNextRow(self, rows):
        row = []
        for i in range(len(rows[-1]) + 1):
            if (i == 0 or i == len(rows[-1])):
                row.append(1)
                continue
            num = rows[-1][i - 1] + rows[-1][i]
            row.append(num)
        rows.append(row)

    def generate(self, numRows):
        rows = []
        rows.append([1])
        if (numRows == 1):
            return rows
        rows.append([1, 1])
        if (numRows == 2):
            return rows
        # for num rows 3 onwards
        for i in range(3, numRows + 1):
            self.generateNextRow(rows)
        return rows
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
