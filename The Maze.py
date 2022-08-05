# The Maze
# https://leetcode.com/problems/the-maze/ 
class Solution(object):
    def isValid(self, row, col, maze):
        if (row >= 0 and row < len(maze)):
            if (col >= 0 and col < len(maze[0])):
                if (maze[row][col] == 0):
                    return True
        return False
    
    def nextMove(self, row, col, maze):
        moves = []
        # start moving left
        newCol = col + 1
        while(self.isValid(row, newCol, maze)):
            newCol += 1
        moves.append([row, newCol-1])
        # start moving right
        newCol = col - 1
        while(self.isValid(row, newCol, maze)):
            newCol -= 1
        moves.append([row, newCol+1])
        # start moving up
        newRow = row - 1
        while(self.isValid(newRow, col, maze)):
            newRow -= 1
        moves.append([newRow+1, col])
        # start moving down
        newRow = row + 1
        while(self.isValid(newRow, col, maze)):
            newRow += 1
        moves.append([newRow-1, col])
        return moves
    
    def dfs(self, row, col, maze, destination, visited):
        #print "move", row, col
        if ([row, col] == destination):
            return True
        # get next moves
        nextMoves = self.nextMove(row, col, maze)
        # go through every move and check if we can reach destination or not
        for move in nextMoves:
            # if move is not current move and not visited
            if (visited[move[0]][move[1]] == False and move != [row, col]):
                # then mark the move visited
                visited[move[0]][move[1]] = True
                # go in dfs
                if (self.dfs(move[0], move[1], maze, destination, visited)):
                    return True
                # backtrack the visited move
                visited[move[0]][move[1]] = False
    
    def hasPath(self, maze, start, destination):
        visited = [[False for col in range(len(maze[0]))] for row in range(len(maze))]
        # Mark start visited
        visited[start[0]][start[1]] = True
        return self.dfs(start[0], start[1], maze, destination, visited)
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        
