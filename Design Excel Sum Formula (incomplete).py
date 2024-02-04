# Design Excel Sum Formula
# https://leetcode.com/problems/design-excel-sum-formula/

class Excel(object):

    def __init__(self, height, width):
        width = self.getColNumber(width) +1
        self.mat = [[0 for col in range(width)] for row in range(height)]
        # key = cell number, val= range
        self.sumCells = {}
        # key = cell, value = if the key is related to any cells in sumCells
        self.relatedCells = {}
        """
        :type height: int
        :type width: str
        """
    
    def getColNumber(self, letter):
        return ord(letter) - ord("A")

    def displayMatrix(self): 
        for row in range(len(self.mat)):
            for col in range(len(self.mat[0])):
                print self.mat[row][col],
            print ""   
        print ""

    def set(self, row, column, val):
        print "set"
        # check if the current cell is related to any other cells
        if (str(row)+column in self.relatedCells):
            # get the related cells and perform their addition again.
            for rCell in self.relatedCells[str(row)+column]:
                r = int(rCell[0])
                c = rCell[1]
                self.get(r, c)
        column = self.getColNumber(column)
        self.mat[row-1][column] = val
        """
        :type row: int
        :type column: str
        :type val: int
        :rtype: None
        """
          

    def get(self, row, column):
        print "get"
        # check if current cell is in sumCells
        if (str(row)+column in self.sumCells):
            # we have to do addition again
            return self.sum(row, column, self.sumCells[str(row)+column])
        column = self.getColNumber(column)
        return self.mat[row-1][column]
        """
        :type row: int
        :type column: str
        :rtype: int
        """
    
    def getCell(self, cell):
        column = self.getColNumber(cell[0])
        row = int(cell[1])-1
        return row, column
    
    def getRange(self, topLeft, bottomRight):
        tlRow, tlCol = self.getCell(topLeft)
        brRow, brCol = self.getCell(bottomRight)
        # perform addition
        addition = 0
        for row in range(tlRow, brRow+1):
            for col in range(tlCol, brCol+1):
                addition += self.mat[row][col]
        return addition
    
    def addRangeToRelatedCells(self, r1, r2, rCell):
        print "in add range to related cells"


    
    def addToRelatedCells(self, cell, rCell):
        print "in add to related cells"
        if (cell not in self.relatedCells):
            self.relatedCells[cell] = []
        self.relatedCells[cell].append(rCell)
        print "related cells", self.relatedCells

    def sum(self, row, column, numbers):
        print "sum"
        # add this to sumCells
        self.sumCells[str(row)+column] = numbers
        addition = 0
        for n in numbers:
            cells = n.split(":")
            if (len(cells) == 1):
                # add this cell to related cells
                self.addToRelatedCells(cells[0], str(row)+column)
                # add single cell to addition
                r, c = self.getCell(cells[0])
                addition += self.mat[r][c]
            else:
                # add this range of cells to related cells
                self.addRangeToRelatedCells(cells[0], cells[1], str(row)+column)
                # we found a range
                addition += self.getRange(cells[0], cells[1])
        # set mat row, column to addition
        column = self.getColNumber(column)
        self.mat[row-1][column] = addition
        print "sum cells", self.sumCells
        self.displayMatrix()
        return self.mat[row-1][column]
        """
        :type row: int
        :type column: str
        :type numbers: List[str]
        :rtype: int
        modify this function to add sum cells to hash map and update them during each set operation
        """
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
