# Minesweeper
# https://app.codesignal.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM
'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]
'''
def isValidCell(matrix, row, col):
    if (row >= 0 and row < len(matrix)):
        if (col >= 0 and col < len(matrix[0])):
            return True
    return False

def getMineCount(matrix, row, col):
    mineCount = 0
    # top Row
    if (isValidCell(matrix, row-1, col-1) and matrix[row-1][col-1] == True):
        mineCount += 1
    if (isValidCell(matrix, row-1, col) and matrix[row-1][col] == True):
        mineCount += 1
    if (isValidCell(matrix, row-1, col+1) and matrix[row-1][col+1] == True):
        mineCount += 1
    # middle row
    if (isValidCell(matrix, row, col-1) and matrix[row][col-1] == True):
        mineCount += 1
    if (isValidCell(matrix, row, col+1) and matrix[row][col+1] == True):
        mineCount += 1
    # bottom row
    if (isValidCell(matrix, row+1, col-1) and matrix[row+1][col-1] == True):
        mineCount += 1
    if (isValidCell(matrix, row+1, col) and matrix[row+1][col] == True):
        mineCount += 1
    if (isValidCell(matrix, row+1, col+1) and matrix[row+1][col+1] == True):
        mineCount += 1
    return mineCount
    
def solution(matrix):
    outputMatrix = []
    for row in range(len(matrix)):
        rowArray = []
        for col in range(len(matrix[0])):
            rowArray.append(getMineCount(matrix, row, col))
        outputMatrix.append(rowArray)
    return outputMatrix
