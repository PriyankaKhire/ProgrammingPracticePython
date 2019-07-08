#Word Search II
#https://leetcode.com/problems/word-search-ii/
class WordSearch(object):
    def __init__(self):
        self.neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    def isValid(self, board, row, col):
        if(row >= 0 and row < len(board)):
            if(col >= 0 and col < len(board[0])):
                return True
        return False

    def dfs(self, row, col, visted, board, word, index, visited):
        if(index == len(word)):
            return True
        for neighbor in self.neighbors:
            new_row = row+neighbor[0]
            new_col = col+neighbor[1]
            if(self.isValid(board, new_row, new_col)):
                if(board[new_row][new_col] == word[index] and visited[new_row][new_col] == 0):
                    visited[new_row][new_col] = 1
                    if(self.dfs(new_row, new_col, visited, board, word, index+1, visited)):
                        return True
                    visited[new_row][new_col] = 0
    
    def ifExists(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == word[0]):
                    visited = [[0 for c in range(len(board[0]))] for r in range(len(board))]
                    visited[row][col] = 1
                    if(self.dfs(row, col, visited, board, word, 1, visited)):
                        return True
        return False
                    
class Solution(object):
    def findWords(self, board, words):
        output = []
        for word in words:
            obj = WordSearch()
            if(obj.ifExists(board, word)):
                output.append(word)
        print output
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
#Main
board = [["a","b"],["a","a"]]
words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]

obj = Solution()
obj.findWords(board, words)

