#Number of Islands II
#https://leetcode.com/problems/number-of-islands-ii/
class Solution(object):
    def __init__(self):
        self.matrix = None
        self.islands = {}
        self.counter = 0
    
    def partOfIslands(self, row, col, islandsCurrentLandPartOf):
        islands = []
        lands = []
        for land in islandsCurrentLandPartOf:
            if not (self.islands[land] in islands):
                islands.append(self.islands[land])
                lands.append(land)
        if(len(islands) == 1):
            self.islands[(row, col)] = islands[0]
        else:
            #now we need to combine these islands to one
            for land in lands:
                self.islands[land] = 'island' + str(self.counter)
            #finally we add our land with this new island
            self.islands[(row, col)] = 'island' + str(self.counter)
            #we increment counter
            self.counter = self.counter + 1
    
    def isValid(self, row, col):
        if(row >= 0 and row < len(self.matrix)):
            if(col >= 0 and col < len(self.matrix[0])):
                return True
        return False
    
    def addLand(self, row, col):
        self.matrix[row][col] = 1
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        partOfIsland = []
        for neighbor in neighbors:
            nRow = row + neighbor[0]
            nCol = col + neighbor[1]
            if(self.isValid(nRow, nCol) and self.matrix[nRow][nCol] == 1):
                partOfIsland.append((nRow, nCol))
        if not(partOfIsland):
            self.islands[(row, col)] = "island"+str(self.counter)
            self.counter = self.counter + 1
        else:
            #if its a part of an island
            self.partOfIslands(row, col, partOfIsland)
            
            
    def countIslands(self):
        islands = []
        for land in self.islands:
            if not(self.islands[land] in islands):
                islands.append(self.islands[land])
        return len(islands)
            
                
        
    def numIslands2(self, m, n, positions):
        self.matrix = [[0 for col in range(n)] for row in range(m)]
        output = []
        for position in positions:
            self.addLand(position[0], position[1])
            number = self.countIslands()
            output.append(number)
        return output
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
#Main
obj = Solution()
obj.numIslands2(3, 3, [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]])
#Expected : [1,2,3,4,3,2,1]
#Current output: [1,2,3,4,3,3,3]
