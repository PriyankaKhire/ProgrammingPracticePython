# -*- coding: utf-8 -*-
'''
We have a m x n 2D grid initialized with three possible values:
-1 - An obstacle.
0 - An exit.
INF - An empty room.

We want to fill each empty room with the distance to its nearest exit.
If it is impossible to reach an exit, it should be filled with INF.

Example:
Given the 2D grid:

INF -1 0 INF
INF INF INF -1
INF -1 INF -1
0 -1 INF INF

We expect the output 2D grid as:

3 -1 0 1
2 2 1 -1
1 -1 2 -1
0 -1 3 4
'''
class Move(object):
    def __init__(self, row, col, moveNum):
        self.row = row
        self. col = col
        self.move = moveNum
        
class Solution(object):

    def createMove(self,row, col, moveNum):
        return Move(row, col, moveNum)
    
    def isValid(self, matrix, row, col, visited):
        if (row >= 0 and row < len(matrix)):
            if (col >=0 and col < len(matrix[0])):
                if (visited[row][col] == 0):
                    if (matrix[row][col] != -1):
                        return True
        return False

    def addMoves(self,moves, matrix, visited, row, col, nextMoveNum):
        if (self.isValid(matrix, row, col, visited)):
            currMove = self.createMove(row, col, nextMoveNum)
            moves.append(currMove)
        
    def nextMoves(self, matrix, row, col, visited, nextMoveNum):
        moves = []
        # Up
        self.addMoves(moves, matrix, visited, row - 1, col, nextMoveNum)
        # Down
        self.addMoves(moves, matrix, visited, row + 1, col, nextMoveNum)
        # Left
        self.addMoves(moves, matrix, visited, row, col + 1, nextMoveNum)
        # Right
        self.addMoves(moves, matrix, visited, row, col - 1, nextMoveNum)
        return moves
        
    def getDistance(self, matrix, visited, queue):
        # get top of queue
        top = queue.pop(0)
        # mark it as visited
        visited[top.row][top.col] = 1
        # if top is exit
        if (matrix[top.row][top.col] == 0):
            return top.move
        # get next moves
        moves = self.nextMoves(matrix, top.row, top.col, visited, top.move + 1)
        # add it to queue
        queue = queue + moves
        return self.getDistance(matrix, visited, queue)
        
    def logic(self, matrix):
        # Find empty room
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (matrix[row][col] == 'inf'):
                    #print row, col
                    visited = [[0 for c in range(len(matrix[0]))] for r in range(len(matrix))]
                    currMove = self.createMove(row, col, 0)
                    distance = self.getDistance(matrix, visited, [currMove])
                    matrix[row][col] = distance
            
    def distanceToNearestExit(self, matrix):
        self.logic(matrix)
        print matrix

# Main
matrix = [
    ['inf', -1, 0, 'inf'],
    ['inf', 'inf', 'inf', -1],
    ['inf', -1, 'inf', -1],
    [0, -1, 'inf', 'inf'] ]

obj = Solution()
obj.distanceToNearestExit(matrix)

