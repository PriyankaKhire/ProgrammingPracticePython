#Game of Life
#https://leetcode.com/problems/game-of-life/
class Solution(object):
    def __init__(self):
        self.neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    
    def isValid(self, row, col, board):
        if(row >= 0 and row < len(board)):
            if(col >= 0 and col < len(board[0])):
                return True
        return False
    
    def deadCellRules(self, row, col, board): 
        #print "Dead Cell", row, col
        liveNeighbors = 0
        for neighbor in self.neighbors:
            new_row = row + neighbor[0]
            new_col = col + neighbor[1]
            if(self.isValid(new_row, new_col, board)):
                if(board[new_row][new_col] == 1 or board[new_row][new_col] == 'l'):
                    liveNeighbors = liveNeighbors + 1
        #print "live neighbor count ", liveNeighbors
        if(liveNeighbors == 3):
            #print "Cell becomes alive"
            board[row][col] = 'o'
        
    def liveCellRules(self, row, col, board):
        #print "Live Cell", row, col
        liveNeighbors = 0
        for neighbor in self.neighbors:
            new_row = row + neighbor[0]
            new_col = col + neighbor[1]
            if(self.isValid(new_row, new_col, board)):
                if(board[new_row][new_col] == 1 or board[new_row][new_col] == 'l'):
                    liveNeighbors = liveNeighbors + 1
        #print "live neighbor count ", liveNeighbors     
        if(liveNeighbors == 2 or liveNeighbors == 3):
            #print "Cell stays alive"
            board[row][col] = 'o'
        elif(liveNeighbors > 2 or liveNeighbors < 3):
            board[row][col] = 'l'
        
    def logic(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == 1 or board[row][col] == 'l'):
                    self.liveCellRules(row, col, board)
                else:
                    self.deadCellRules(row, col, board)
            
    def gameOfLife(self, board):
        self.logic(board)
        print board
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
