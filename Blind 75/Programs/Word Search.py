# Word Search
# https://leetcode.com/problems/word-search/
class Solution(object):
                
    def findIfAllLettersInBoard(self, board, word):
        letterHash = {}
        # Count all letters on the board and put it in a hash table.
        for row in range(len(board)):
            for col in range(len(board[0])):
                if not (board[row][col] in letterHash):
                    letterHash[board[row][col]] = 0
                letterHash[board[row][col]] = letterHash[board[row][col]] + 1
        # see if the word has enough letters that are present on the board
        for letter in word:
            # all letters from the word are not present on the board
            if (letter not in letterHash or letterHash[letter] == 0):
                return False
            letterHash[letter] = letterHash[letter] - 1
        return True
            
    def isValid(self, row, col, board, visited):
        if (row >= 0 and row < len(board)):
            if (col >= 0 and col < len(board[0])):
                if ([row, col] not in visited):
                    return True
        
    def nextMoves(self, board, row, col, visited):
        move = []
        # up
        if (self.isValid(row-1, col, board, visited)):
            move.append([row-1, col])
        # down
        if (self.isValid(row+1, col, board, visited)):
            move.append([row+1, col])
        # left
        if (self.isValid(row, col-1, board, visited)):
            move.append([row, col-1])
        # right
        if (self.isValid(row, col+1, board, visited)):
            move.append([row, col+1])
        # return moves
        return move
    
    def dfs(self, board, row, col, visited, word, index):
        if (index == len(word)):
            return True
        # get next moves
        moves = self.nextMoves(board, row, col, visited)
        # iterate through next moves
        for move in moves:
            # if move has not been visited
            if (move not in visited):
                # if the cell has same letter as letter at word index
                if (board[move[0]][move[1]] == word[index]):
                    # Mark current row, col visited in the function call, this helps in backtracking.
                    if (self.dfs(board, move[0], move[1], visited+[[row, col]], word, index+1)):
                        return True
        
    def exist(self, board, word):
        # Edge case to see if all letters in word are present in board
        if not(self.findIfAllLettersInBoard(board, word)):
            return False
        # Search for word in board
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (board[row][col] == word[0]):
                    if (self.dfs(board, row, col, [], word, 1)):
                        return True
        return False
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
