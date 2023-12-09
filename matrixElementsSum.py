# matrixElementsSum
# https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
def removeRoomsBelowHauntedRooms(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (matrix[row][col] <= 0):
                # make cell below current cell -1
                if (row+1 < len(matrix) and matrix[row+1][col] > 0):
                    matrix[row+1][col] = -1
            print matrix[row][col],
        print ""
        
def getCost(matrix):
    cost = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (matrix[row][col] > 0):
                cost += matrix[row][col]
    return cost
    
def solution(matrix):
    removeRoomsBelowHauntedRooms(matrix)
    return getCost(matrix)
