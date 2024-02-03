# Word Search

class Solution(object):
    def isValid(self, board, row, col, letter, visited):
        if (row >= 0 and row < len(board)):
            if (col >=0 and col < len(board[0])):
                if ([row, col] not in visited and board[row][col] == letter):
                    return True
        return False
    
    def nextMove(self, row, col, letter, board, visited):
        moves = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        validMoves = []
        for m in moves:
            if (self.isValid(board, row+m[0], col+m[1], letter, visited)):
                validMoves.append([row+m[0], col+m[1]])
        return validMoves
    
    def dfs(self, board, row, col, word, index, visited):
        if (board[row][col] == word[index] and index == len(word)-1):
            return True
        if (board[row][col] != word[index]):
            return False
        # if current cell == word[index]
        moves = self.nextMove(row, col, word[index+1], board, visited)
        for m in moves:
            if (self.dfs(board, m[0], m[1], word, index+1, visited+[[m[0], m[1]]])):
                return True
            # backtracking

    def exist(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[0])):
                # remember to mark cells visited
                if (self.dfs(board, row, col, word, 0, [[row, col]])):
                    return True
        return False
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
