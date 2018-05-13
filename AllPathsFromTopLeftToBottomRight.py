#Print all possible paths from top left to bottom right of a mXn matrix
#https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/

def is_valid_move(row, col, matrix):
    if(row >= 0 and row < len(matrix)):
        if(col >= 0 and col < len(matrix[0])):
            return True
    return False

def next_move(move, row, col, matrix):
    if move == "right":
        col = col +1    
    if move == "down":
        row = row +1
    return row, col

def solution(matrix, row, col, path):
    moves = ["right", "down"]
    if(row == len(matrix)-1 and col == len(matrix[0])-1):
        print path
        return
    for move in moves:
        n_row, n_col = next_move(move, row, col, matrix)
        if(is_valid_move(n_row, n_col, matrix)):
            path.append(matrix[n_row][n_col])
            solution(matrix, n_row, n_col, path)
            #Back track
            path.pop()


#Main
matrix = [[1,2,3],[4,5,6]]
solution(matrix, 0, 0, [matrix[0][0]])
print "---"
matrix = [[1,2],[3,4]]
solution(matrix, 0, 0, [matrix[0][0]])
