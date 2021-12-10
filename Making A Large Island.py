# Making A Large Island
# https://leetcode.com/problems/making-a-large-island/

class Solution(object):
    def __init__(self):
        # key = groupId, val = size
        self.groupIndex = {}
    
    def isValid(self, row, col, grid):
        if(row >= 0 and row < len(grid)):
            if (col >= 0 and col < len(grid[0])):
                return True
        return False
    
    def getNextMove(self, row, col, grid):
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        validMoves = []
        for m in moves:
            newR = row + m[0]
            newC = col + m[1]
            if(self.isValid(newR, newC, grid)):
                validMoves.append([newR, newC])
        return validMoves
    
    def dfs(self, row, col, grid, ID, size):
        # mark current visited by changing it to ID
        grid[row][col] = ID
        # increment the size
        size[0] = size[0] + 1
        # get next moves
        moves = self.getNextMove(row, col, grid)
        for m in moves:
            if (grid[m[0]][m[1]] == 1):
                self.dfs(m[0], m[1], grid, ID, size)
    
    def assignIndex(self, grid):
        # random ID
        ID = 2
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 1):
                    # start assigning it Id and calculate it's size
                    size = [0]
                    self.dfs(row, col, grid, ID, size)
                    # add it to hash
                    self.groupIndex[ID] = size[0]
                    # increment the ID to make it unique for next group
                    ID = ID + 1
        
        
    def largestIsland(self, grid):
        self.assignIndex(grid)
        print grid
        maxArea = 0
        # for every 0 check up down left right for it's adjacent islands
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 0):
                    currArea = 0
                    # set variable to keep track of all the island groups we have seen so far
                    visitedID = set()
                    # get the next valid neighbors
                    neighbors = self.getNextMove(row, col, grid)
                    # for all the neighbors
                    for n in neighbors:
                        currID = grid[n[0]][n[1]]
                        if (currID != 0 and (currID not in visitedID)):
                            currArea = currArea + self.groupIndex[currID]
                            visitedID.add(currID)
                    # add 1 for current cell
                    currArea = currArea + 1
                    # compare with maxArea
                    maxArea = max(maxArea, currArea)
        # get max value from hash table
        maxAreaFromHashTable = 0
        if(self.groupIndex):
            maxAreaFromHashTable = max(self.groupIndex.values())
        return max(maxAreaFromHashTable, maxArea)
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
