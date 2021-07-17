# Minesweeper
# https://leetcode.com/problems/minesweeper/

class Solution(object):
    def changeSquare(self, board, click, value):
        board[click[0]][click[1]] = value
    
    def isValid(self, board, row, col):
        if(row >= 0 and row < len(board)):
            if(col >=0 and col < len(board[0])):
                return True
    
    def getNextMove(self, board, click):
        moves = []
        # up
        if (self.isValid(board, click[0]-1, click[1])):
            moves.append([click[0]-1, click[1]])
        # down
        if (self.isValid(board, click[0]+1, click[1])):
            moves.append([click[0]+1, click[1]])
        # left
        if (self.isValid(board, click[0], click[1]-1)):
            moves.append([click[0], click[1]-1])
        # right
        if (self.isValid(board, click[0], click[1]+1)):
            moves.append([click[0], click[1]+1])
        # up, right
        if (self.isValid(board, click[0]-1, click[1]+1)):
            moves.append([click[0]-1, click[1]+1])
        # up, left
        if (self.isValid(board, click[0]-1, click[1]-1)):
            moves.append([click[0]-1, click[1]-1])
        # down, right
        if (self.isValid(board, click[0]+1, click[1]+1)):
            moves.append([click[0]+1, click[1]+1])
        # down, left
        if (self.isValid(board, click[0]+1, click[1]-1)):
            moves.append([click[0]+1, click[1]-1])
        return moves
    
    def isMine(self, board, click):
        if(board[click[0]][click[1]] == 'M'):
            return True
        
    def checkForMine(self, board, click):
        nextMoves = self.getNextMove(board, click)
        numberOfMines = 0
        for move in nextMoves:
            if(self.isMine(board, move)):
                numberOfMines = numberOfMines+1
        return numberOfMines
        
    def clickBoard(self, board, click):
        #print "Currently clicking", click
        if(self.isMine(board, click)):
            self.changeSquare(board, click, 'X')
            return
        # if square has mine next to it
        numberOfMines = self.checkForMine(board, click)
        if(numberOfMines > 0):
            self.changeSquare(board, click, str(numberOfMines))
            return
        # change current square to B
        self.changeSquare(board, click, 'B')
        # get next moves
        nextMoves = self.getNextMove(board, click)
        for move in nextMoves:
            # only visit if it's not been clicked before
            if(board[move[0]][move[1]] == 'E'):
                self.clickBoard(board, move)
        
            
    def updateBoard(self, board, click):
        self.clickBoard(board, click)
        return board
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
