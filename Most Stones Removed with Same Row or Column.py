# Most Stones Removed with Same Row or Column
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
class Solution(object):
    def __init__(self):
        self.sameRow = {}
        self.sameCol = {}
        self.matrix = None
        self.visited = None

    def fillHash(self, stones):
        # we put key as row/col coordinate and value as index of the stone
        for stone in range(len(stones)):
            r = stones[stone][0]
            c = stones[stone][1]
            if not(r in self.sameRow):
                self.sameRow[r] = [stone]
            else:
                self.sameRow[r].append(stone)
            if not(c in self.sameCol):
                self.sameCol[c] = [stone]
            else:
                self.sameCol[c].append(stone)

    def fillGraphMatrix(self, stones):
        self.matrix = [[0 for col in range(len(stones))] for row in range(len(stones))]
        for i in range(len(stones)):
            r = stones[i][0]
            c = stones[i][1]
            # get the row from matrix and draw an edge towards which ever stone is sharing that row with our current stone.
            for jr in self.sameRow[r]:
                self.matrix[i][jr] = 1
            for jc in self.sameCol[c]:
                self.matrix[i][jc] = 1

    def dfs(self, stone, stack):
        stack.append(stone)
        # complete it.
        self.visited[stone] = True
        for adjacentStone in range(len(self.matrix)):
            if(self.matrix[stone][adjacentStone] == 1 and self.visited[adjacentStone] == None):
                self.dfs(adjacentStone, stack)
                
        
    def removeStones(self, stones):
        print stones
        self.fillHash(stones)
        self.fillGraphMatrix(stones)
        self.visited = [None for i in range(len(stones))]
        # if stack has more than one element then we can remove all elements except last one
        output = 0
        for i in range(len(stones)):
            if(self.visited[i] == None):
                stack = []
                self.dfs(i, stack)
                if(len(stack) > 1):
                    output = output + len(stack)-1
        print output
        """
        :type stones: List[List[int]]
        :rtype: int
        """
# Main
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
obj = Solution()
obj.removeStones(stones)
