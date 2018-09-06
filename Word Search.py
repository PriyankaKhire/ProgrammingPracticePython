#Word Search
#https://leetcode.com/problems/word-search/description/

class Solution(object):
    def isValid(self, row, col, matrix, letter):
        if(row >= 0 and row < len(matrix)):
            if(col >=0 and col < len(matrix[0])):
                if(matrix[row][col] == letter):
                    return True
        return False
    
    def nextMove(self, row, col, matrix, letter):
        output = []
        #up
        if(self.isValid(row-1, col, matrix, letter)):
            output.append([row-1, col])
        #down
        if(self.isValid(row+1, col, matrix, letter)):
            output.append([row+1, col])
        #left
        if(self.isValid(row, col-1, matrix, letter)):
            output.append([row, col-1])
        #right
        if(self.isValid(row, col+1, matrix, letter)):
            output.append([row, col+1])
        return output

    def dfs(self, word, matrix, index, row, col, visited):
        if(index == len(word)):
            return True
        nextMoves = self.nextMove(row, col, matrix, word[index])
        for move in nextMoves:
            if move in visited:
                continue
            r = move[0]
            c = move[1]
            visited.append([r,c])
            if(self.dfs(word, matrix, index+1, r, c, visited)):
                return True
            #backtrack
            visited.pop()
    
    def exist(self, board, word):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == word[0]):
                    if (self.dfs(word, board, 1, row, col, [[row, col]])):
                        return True
        return False
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

#Main
m = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
m = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
o = Solution()
print o.exist(m, "eat")
