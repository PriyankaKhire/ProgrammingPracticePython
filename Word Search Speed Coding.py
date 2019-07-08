#Word Search
#https://leetcode.com/problems/word-search/
class Solution(object):
    def __init__(self):
        self.neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def isValid(self, row, col, board):
        if(row >= 0 and row < len(board)):
            if(col >= 0 and col < len(board[0])):
                return True
        return False

    def dfs(self, row, col, word, index, board, visited):
        if(index == len(word)):
            return True
        for neighbor in self.neighbors:
            new_row = row+neighbor[0]
            new_col = col+neighbor[1]
            if(self.isValid(new_row, new_col, board)):
                if(board[new_row][new_col] == word[index] and visited[new_row][new_col] == 0):
                    visited[new_row][new_col] = 1
                    if(self.dfs(new_row, new_col, word, index+1, board, visited)):
                        return True
                    visited[new_row][new_col] = 0
        

    def logic(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == word[0]):
                    visited = [[0 for c in range(len(board[0]))] for r in range(len(board))]
                    visited[row][col] = 1
                    if(self.dfs(row, col, word, 1, board, visited)):
                        return True
        return False
                    
    def exist(self, board, word):
        print self.logic(board, word)
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
#Main
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
board = [["a","a"]]
obj = Solution()
obj.exist(board, "aaa")
