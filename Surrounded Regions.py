#Surrounded Regions
#https://leetcode.com/problems/surrounded-regions/
class Solution(object):
    def displayBoard(self, board):
        for row in range(len(board)):
            print board[row]
        print "\n"

    def isValid(self, row, col, board, beforeFlipLetter):
        if(row >= 0 and row < len(board)):
            if(col >= 0 and col < len(board[0])):
                if(board[row][col] == beforeFlipLetter):
                    return True
        return False

    def flipCells(self, row, col, flipLetter, beforeFlipLetter, board):
        #Flip current letter
        board[row][col] = flipLetter
        directions = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]
        for direction in directions:
            if(self.isValid(direction[0], direction[1], board, beforeFlipLetter)):
               self.flipCells(direction[0], direction[1], flipLetter, beforeFlipLetter, board)
        

    def findBorderCells(self, board, flipLetter, beforeFlipLetter):
        for col in range(len(board[0])):
            if(board[0][col] == beforeFlipLetter):
                self.flipCells(0, col, flipLetter, beforeFlipLetter, board)
            if(board[len(board)-1][col] == beforeFlipLetter):
                self.flipCells(len(board)-1, col, flipLetter, beforeFlipLetter, board)
        for row in range(len(board)):
            if(board[row][0] == beforeFlipLetter):
                self.flipCells(row, 0, flipLetter, beforeFlipLetter, board)
            if(board[row][len(board[0])-1] == beforeFlipLetter):
                self.flipCells(row, len(board[0])-1, flipLetter, beforeFlipLetter, board)

    def findInnerCells(self, board):
        for row in range(1, len(board)-1):
            for col in range(1, len(board[0])-1):
                if(board[row][col] == 'O'):
                    self.flipCells(row, col, 'X', 'O', board)            
                         
            
    def solve(self, board):
        if not board:
            return
        self.findBorderCells(board, 'b', 'O')
        self.displayBoard(board)
        self.findInnerCells(board)
        self.displayBoard(board)
        self.findBorderCells(board, 'O', 'b')
        self.displayBoard(board)
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
#Main
board = [
    ["X","X","X","X"],
    ["X","X","O","X"],
    ["O","O","X","X"],
    ["O","O","X","X"]
    ]
obj = Solution()
obj.solve(board)
