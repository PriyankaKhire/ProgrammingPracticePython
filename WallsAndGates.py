# Walls and Gates
# https://leetcode.com/problems/walls-and-gates/
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
        if not queue:
            return
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
                if (matrix[row][col] == 2147483647):
                    #print row, col
                    visited = [[0 for c in range(len(matrix[0]))] for r in range(len(matrix))]
                    currMove = self.createMove(row, col, 0)
                    distance = self.getDistance(matrix, visited, [currMove])
                    if distance:
                        matrix[row][col] = distance
                    
    def wallsAndGates(self, rooms):
        self.logic(rooms)
        print rooms
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        
