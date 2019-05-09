#Sliding Puzzle
#https://leetcode.com/problems/sliding-puzzle/
import copy
class BFS(object):

    def isValid(self, row, col, board, prevPos):
        #print "Is row ", row, " and col ", col, " valid ?",
        if(prevPos != [row, col]):
            if(row >= 0 and row < len(board)):
                if(col >= 0 and col < len(board[0])):
                    #print "Yes"
                    return True
        #print "No"
        return False

    def boardSwap(self, board, srcPos, destPos):
        board[srcPos[0]][srcPos[1]], board[destPos[0]][destPos[1]] = board[destPos[0]][destPos[1]], board[srcPos[0]][srcPos[1]]
        return board
    
    def logic(self, queue):
        if not queue:
            print "-1"
            return
        top = queue.pop(0)
        board = top[0]
        zeroPosition = top[1]
        moveNumber = top[2]
        prevPos = top[3]
        if(board == [[1,2,3],[4,5,0]]):
            print "Found the board in ", moveNumber, " moves"
            return
        #print "Queue top board is ", board, " zero position is ", zeroPosition, " move number is ", moveNumber, " previous Position ", prevPos
        #up
        if(self.isValid(zeroPosition[0]-1, zeroPosition[1], board, prevPos)):
           #print "going up "
           upBoard = copy.deepcopy(board)
           upBoard = self.boardSwap(upBoard, zeroPosition, [zeroPosition[0]-1, zeroPosition[1]] )
           #print "Board ", board ," after swapping is ", upBoard, " Position is ", [zeroPosition[0]-1, zeroPosition[1]]
           queue.append([upBoard, [zeroPosition[0]-1, zeroPosition[1]], moveNumber+1, zeroPosition])
           #board = self.boardSwap(board, [zeroPosition[0]-1, zeroPosition[1]], zeroPosition )
        #down
        if(self.isValid(zeroPosition[0]+1, zeroPosition[1], board, prevPos)):
           #print "going down "
           downBoard = copy.deepcopy(board)
           downBoard = self.boardSwap(downBoard, zeroPosition, [zeroPosition[0]+1, zeroPosition[1]] )
           #print "Board ", board ," after swapping is ",downBoard, " Position is ", [zeroPosition[0]+1, zeroPosition[1]]
           queue.append([downBoard, [zeroPosition[0]+1, zeroPosition[1]], moveNumber+1, zeroPosition])
           #board = self.boardSwap(board, [zeroPosition[0]+1, zeroPosition[1]], zeroPosition )
        #left
        if(self.isValid(zeroPosition[0], zeroPosition[1]-1, board, prevPos)):
           #print "going left"
           leftBoard = copy.deepcopy(board)
           leftBoard = self.boardSwap(leftBoard, zeroPosition, [zeroPosition[0], zeroPosition[1]-1] )
           #print "Board ", board ," after swapping is ",leftBoard, " Position is ", [zeroPosition[0], zeroPosition[1]-1]
           queue.append([leftBoard, [zeroPosition[0], zeroPosition[1]-1], moveNumber+1, zeroPosition])
           #board = self.boardSwap(board, [zeroPosition[0], zeroPosition[1]-1], zeroPosition )
        #right
        if(self.isValid(zeroPosition[0], zeroPosition[1]+1, board, prevPos)):
           #print "going right"
           rightBoard = copy.deepcopy(board)
           rightBoard = self.boardSwap(rightBoard, zeroPosition, [zeroPosition[0], zeroPosition[1]+1] )
           #print "Board ", board ," after swapping is ",rightBoard, " Position is ", [zeroPosition[0], zeroPosition[1]+1]
           queue.append([rightBoard, [zeroPosition[0], zeroPosition[1]+1], moveNumber+1, zeroPosition])
           #board = self.boardSwap(board, [zeroPosition[0], zeroPosition[1]+1], zeroPosition )
        self.logic(queue)
        
    def slidingPuzzle(self, board):
        zeroPosition = []
        #find position of zero
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] == 0):
                    zeroPosition = [row, col]
        self.logic([[board, zeroPosition, 0, None]])
        """
        :type board: List[List[int]]
        :rtype: int
        """

#Main
'''
obj1 = BFS()
obj1.slidingPuzzle([[1,2,3],[4,0,5]])

obj2 = BFS()
obj2.slidingPuzzle([[4,1,2],[5,0,3]])
'''
obj3 = BFS()
obj3.slidingPuzzle([[1,2,3],[5,4,0]])

'''
obj4 = BFS()
obj4.slidingPuzzle([[3,2,4],[1,5,0]])
'''
