# Word Search II

class Solution(object):
    def isValid(self, row, col, board, letter, visited):
        if (row >= 0 and row < len(board)):
            if (col >= 0 and col < len(board[0])):
                if ([row, col] not in visited and board[row][col] == letter):
                    return True
        return False
    
    def nextMove(self, row, col, letter, visited, board):
        moves = [[0,1], [0, -1], [1, 0], [-1, 0]]
        validMoves = []
        for m in moves:
            if (self.isValid(row+m[0], col+m[1], board, letter, visited)):
                validMoves.append([row+m[0], col+m[1]])
        return validMoves
    
    def dfs(self, row, col, board, word, index, visited):
        print row, col, board[row][col], word[index], visited
        if (board[row][col] == word[index] and index == len(word)-1):
            return True
        if (board[row][col] != word[index]):
            return False
        moves = self.nextMove(row, col, word[index+1], visited, board)
        for m in moves:
            # mark m as visited
            if (self.dfs(m[0], m[1], board, word, index+1, visited+[[m[0], m[1]]])):
                return True
            # backtracking

    def findWords(self, board, words):
        output = []
        for w in words:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if (board[row][col] == w[0] and w not in output):
                        print "word", w, "board cell", row, col
                        if (self.dfs(row, col, board, w, 0, [[row, col]])):
                            output.append(w)
        return output
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
