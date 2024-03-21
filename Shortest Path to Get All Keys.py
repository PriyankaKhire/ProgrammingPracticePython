# Shortest Path to Get All Keys
# https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
class Solution(object):
    def __init__(self):
        # key = cell, value = [list of key holding states]
        self.visited = {}
    
    def isLockKey(self, char):
        if (char == 'a'):
            return True
        if (char == 'b'):
            return True
        if (char == 'c'):
            return True
        if (char == 'd'):
            return True
        if (char == 'e'):
            return True
        if (char == 'f'):
            return True
        return False
    
    def isLock(self, char):
        if (char == 'A'):
            return True, 0
        if (char == 'B'):
            return True, 1
        if (char == 'C'):
            return True, 2
        if (char == 'D'):
            return True, 3
        if (char == 'E'):
            return True, 4
        if (char == 'F'):
            return True, 5
    
    def haveKeyToLock(self, char, currentState):
        flag, index = self.isLock(char)
        # if current character is not a lock
        if (not flag):
            return False
        key = currentState[index]
        # if current char is a lock and we have the key
        if (key == '1'):
            return True
        # if we don't have the key
        return False
    
    def isValid(self, grid, row, col, currentState):
        if (row >= 0 and row < len(grid)):
            if (col >= 0 and col < len(grid[0])):
                # if it's a wall
                if (grid[row][col] == "#"):
                    return False
                # if cell not visited
                key = self.makeKey(row, col)
                if ((key not in self.visited)):
                    # if it's a . then visit it
                    if (grid[row][col] == '.'):
                        return True
                    # if it's a key to the lock
                    if (self.isLockKey(grid[row][col])):
                        return True
                    # if you have the key to the lock
                    if (self.haveKeyToLock(grid[row][col], currentState)):
                        return True
                else:
                    # if cell visited
                    # then check which state we visited it in
                    if (currentState not in self.visited[key]):
                        return True
        return False
    
    def makeKey(self, row, col):
        return str(row)+str(col)
    
    def nextMove(self, grid, row, col, currentState, distance):
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        validMoves = []
        for m in moves:
            if (self.isValid(grid, row+m[0], col+m[1], currentState)):
                validMoves.append([row+m[0], col+m[1], distance+1, currentState])
        return validMoves
    
    def changeState(self, char, currentState):
        if (self.isLockKey(char)):
            index = ord(char) - ord('a')
            currentState = currentState[:index] + '1' + currentState[index+1:]
        return currentState
    
    def bfs(self, grid, queue, desiredState, output):
        # if at any point the queue is empty then return
        if not queue:
            #print "queue is empty"
            return
        # get the top
        [topR, topC, distance, currentState] = queue.pop(0)
        #print "current char",grid[topR][topC], "at distance", distance
        #print currentState, queue
        # change current state depending on what's on current cell
        currentState = self.changeState(grid[topR][topC], currentState)
        # if at any given point of time we have collected all keys
        if (currentState == desiredState):
            #print "desired state achived", distance
            output[0] = distance
            return
        #print "current State", currentState
        # mark it as visited
        key = self.makeKey(topR, topC)
        if (key not in self.visited):
            self.visited[key] = []
        self.visited[key].append(currentState)
        #print "visited", self.visited
        # get all valid moves
        validMoves = self.nextMove(grid, topR, topC, currentState, distance)
        #print "next moves", validMoves
        # add it to the queue
        queue += validMoves
        #print "*"*15
        # do bfs
        self.bfs(grid, queue, desiredState, output)
        
    def getDesiredState(self, grid):
        desiredState = "000000"
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                desiredState = self.changeState(grid[row][col], desiredState)
        return desiredState

    def findStart(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == "@"):
                    return row, col

    def shortestPathAllKeys(self, grid):
        r,c = self.findStart(grid)
        # 6 zeros because there cannot be more than 6 keys
        currentState = "000000"
        queue = [[r,c,0, currentState]]
        desiredState = self.getDesiredState(grid)
        output = [-1]
        self.bfs(grid, queue, desiredState, output)
        return output[0]
        """
        :type grid: List[str]
        :rtype: int
        """
        