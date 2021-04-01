# Number of Distinct Islands
# https://leetcode.com/problems/number-of-distinct-islands/
class IslandStructure(object):
    def __init__(self, row, col, structure):
        self.row = row
        self.col = col
        self.structure = structure
        
class Solution(object):
    def __init__(self):
        self.structure = []
        
    def isValid(self, row, col, grid):
        if (row >= 0 and row < len(grid)):
            if (col >= 0 and col < len(grid[0])):
                # if there is land
                if (grid[row][col] == 1):
                    return True
        return False
    
    def addToMoves(self, row, col, grid, moves, structure):
        if (self.isValid(row, col, grid)):
            islandStructureObject = IslandStructure(row, col, structure)
            moves.append(islandStructureObject)
        
    def nextMoves(self, row, col, grid):
        moves = []
        # Up
        self.addToMoves(row-1, col, grid, moves, "Up")
        # Down
        self.addToMoves(row+1, col, grid, moves, "Down")
        # Left
        self.addToMoves(row, col-1, grid, moves, "Left")
        # Right
        self.addToMoves(row, col+1, grid, moves, "Right")
        return moves

    def dfs(self, row, col, grid, structure):
        # If the current cell is already visited then return
        if (grid[row][col] == 0):
            return
        # Mark current visited
        grid[row][col] = 0
        # get next moves
        moves = self.nextMoves(row, col, grid)
        for move in moves:
            structure.append(move.structure)
            self.dfs(move.row, move.col, grid, structure)
            # Unique addition to island structure to see where I have backtracked.
            structure.append('Backtrack')

    def addToStructure(self, structure):
        print structure
        if not(structure in self.structure):
            self.structure.append(structure)
        
    def numDistinctIslands(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 1):
                    structure = ['Initial']
                    self.dfs(row, col, grid, structure)
                    self.addToStructure(structure)
        print "Number of unique islands are", len(self.structure)
        """
        :type grid: List[List[int]]
        :rtype: int
        """

# Main
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
    ]
obj = Solution()
obj.numDistinctIslands(grid)

grid = [
    [1,1,0,1,1],
    [1,0,0,0,0],
    [0,0,0,0,1],
    [1,1,0,1,1]
    ]
obj = Solution()
obj.numDistinctIslands(grid)

grid = [
    [1,1,0],
    [0,1,1],
    [0,0,0],
    [1,1,1],
    [0,1,0]]

obj = Solution()
obj.numDistinctIslands(grid)
