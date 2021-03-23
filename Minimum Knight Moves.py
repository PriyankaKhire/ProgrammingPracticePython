# https://leetcode.com/problems/minimum-knight-moves/
# Minimum Knight Moves

class Move(object):
    def __init__(self, move, moveNumber):
        self.move = move
        self.moveNumber = moveNumber
        
class Solution(object):
    def moves(self, x, y, moveNumber):
        moveList = []
        # up
        # left
        moveList.append([x-1, y+2])
        # right
        moveList.append([x+1, y+2])
        
        # left
        # up
        moveList.append([x-2, y+1])
        # down
        moveList.append([x-2, y-1])
        
        # right
        # up
        moveList.append([x+2, y+1])
        # down
        moveList.append([x+2, y-1])
        
        # down
        # left
        moveList.append([x-1, y-2])
        # right
        moveList.append([x+1, y-2])
        
        # make it into move object
        newMoveList = []
        for m in moveList:
            newMove = Move(m, moveNumber)
            newMoveList.append(newMove)
        return newMoveList
    
    def bfs(self, queue, x, y):
        if not queue:
            return
        topMoveObj = queue.pop(0)
        #print "move", topMoveObj.move
        #print "move number", topMoveObj.moveNumber
        if (topMoveObj.move[0] == x and topMoveObj.move[1] == y):
            return topMoveObj.moveNumber
        nextMoves = self.moves(topMoveObj.move[0], topMoveObj.move[1], topMoveObj.moveNumber+1)
        queue = queue+nextMoves
        #print "Contents of queue"
        #for m in queue:
        #    print m.move
        return self.bfs(queue, x, y)
    
        
    def minKnightMoves(self, x, y):
        startMove = Move([0,0], 0)
        queue = [startMove]
        return self.bfs(queue, x, y)
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
