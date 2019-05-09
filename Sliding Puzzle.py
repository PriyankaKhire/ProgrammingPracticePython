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
class BFS2(object):
    def __init__(self):
        #below hash map tells if 0 is at ith position in string what directions can it move
        #example if 2 d list is [[1,2,3],[4,0,5]] here 0 is located at [1,1] location
        #when we convert this 2d list to string 123405 it is located at 4th index in string
        #we know it can move up, left, right so in a string it can have positions at index 1 for up, 3 for left and 5 for right
        self.moves = {0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4], 4:[3,1,5], 5:[2,4]}
        self.seen = {}

    def swap(self, c, src, dst):
        c = list(c)
        c[src], c[dst] = c[dst], c[src]
        return ''.join(c)
        
    def convert2DListToStr(self, lst):
        return ''.join(str(x) for x in sum(lst, []))

    def logic(self, queue):
        #print "Queue is ",queue,
        if not queue:
            print "not found"
            return -1
        top = queue.pop(0)
        string = top[0]
        zeroPosition = top[1]
        moveNumber = top[2]
        #print " top string is ", string, " zero position is ", zeroPosition, " move number ", moveNumber
        if(string == "123450"):
            print "found in ", moveNumber, " moves "
            return moveNumber
        for move in self.moves[zeroPosition]:
            #print "move to swap is ", move
            newStr = self.swap(string, zeroPosition, move)
            #print "New string after swapping is ", newStr
            if not (newStr in self.seen):
                self.seen[string].append(newStr)
                self.seen[newStr] = []
                queue.append([newStr, move, moveNumber+1])
        return self.logic(queue)
        
    
    def slidingPuzzle(self, board):
        string = self.convert2DListToStr(board)
        zeroPos = string.find('0')
        self.seen[string] = []
        print self.logic([[string, zeroPos, 0]])
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

obj3 = BFS()
obj3.slidingPuzzle([[1,2,3],[5,4,0]])


obj4 = BFS()
obj4.slidingPuzzle([[3,2,4],[1,5,0]])

obj21 = BFS2()
obj21.slidingPuzzle([[1,2,3],[4,0,5]])

obj22 = BFS2()
obj22.slidingPuzzle([[4,1,2],[5,0,3]])
'''
obj23 = BFS2()
obj23.slidingPuzzle([[1,2,3],[5,4,0]])
'''
obj24 = BFS2()
obj24.slidingPuzzle([[3,2,4],[1,5,0]])
'''

