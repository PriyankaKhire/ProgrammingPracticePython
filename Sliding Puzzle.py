#Sliding Puzzle
#https://leetcode.com/problems/sliding-puzzle/
class BFS(object):

    def isValid(self, row, col, board):
        print "Is row ", row, " and col ", col, " valid ?", 
        if(row >= 0 and row < len(board)):
            if(col >= 0 and col < len(board[0])):
                print "Yes"
                return True
        print "No"
        return False

    def boardSwap(self, board, srcPos, destPos):
        board[srcPos[0]][srcPos[1]], board[destPos[0]][destPos[1]] = board[destPos[0]][destPos[1]], board[srcPos[0]][srcPos[1]]
        return board
    
    def logic(self, queue):
        if not queue:
            return
        top = queue.pop(0)
        board = top[0]
        zeroPosition = top[1]
        moveNumber = top[2]
        print "Queue top board is ", board, " zero position is ", zeroPosition, " move number is ", moveNumber
        #up
        if(self.isValid(zeroPosition[0]-1, zeroPosition[1], board)):
           print "going up "
           print "Board ", board ,
           upBoard = self.boardSwap(board, zeroPosition, [zeroPosition[0]-1, zeroPosition[1]] )
           print " after swapping is ", upBoard, " Position is ", [zeroPosition[0]-1, zeroPosition[1]]
           queue.append([upBoard, [zeroPosition[0]-1, zeroPosition[1]], moveNumber+1])
           board = self.boardSwap(board, [zeroPosition[0]-1, zeroPosition[1]], zeroPosition )
        #down
        if(self.isValid(zeroPosition[0]+1, zeroPosition[1], board)):
           print "going down "
           print "Board ", board ,
           downBoard = self.boardSwap(board, zeroPosition, [zeroPosition[0]+1, zeroPosition[1]] )
           print " after swapping is ",downBoard, " Position is ", [zeroPosition[0]+1, zeroPosition[1]]
           queue.append([downBoard, [zeroPosition[0]+1, zeroPosition[1]], moveNumber+1])
           board = self.boardSwap(board, [zeroPosition[0]+1, zeroPosition[1]], zeroPosition )
        #left
        if(self.isValid(zeroPosition[0], zeroPosition[1]-1, board)):
           print "going left"
           print "Board ", board ,
           leftBoard = self.boardSwap(board, zeroPosition, [zeroPosition[0], zeroPosition[1]-1] )
           print " after swapping is ",leftBoard, " Position is ", [zeroPosition[0], zeroPosition[1]-1]
           queue.append([leftBoard, [zeroPosition[0], zeroPosition[1]-1], moveNumber+1])
           board = self.boardSwap(board, [zeroPosition[0], zeroPosition[1]-1], zeroPosition )
        #right
        if(self.isValid(zeroPosition[0], zeroPosition[1]+1, board)):
           print "going right"
           print "Board ", board ,
           rightBoard = self.boardSwap(board, zeroPosition, [zeroPosition[0], zeroPosition[1]+1] )
           print " after swapping is ",rightBoard, " Position is ", [zeroPosition[0], zeroPosition[1]+1]
           queue.append([rightBoard, [zeroPosition[0], zeroPosition[1]+1], moveNumber+1])
           board = self.boardSwap(board, [zeroPosition[0], zeroPosition[1]+1], zeroPosition )
        self.logic(queue)
        
    def slidingPuzzle(self, board):
        zeroPosition = []
        #find position of zero
        for row in range(len(board)):
            for col in range(len(board)):
                if(board[row][col] == 0):
                    zeroPosition = [row, col]
        self.logic([[board, zeroPosition, 0]])
        """
        :type board: List[List[int]]
        :rtype: int
        """

#Main
obj1 = BFS()
obj1.slidingPuzzle([[4,1,2],[5,0,3]])
