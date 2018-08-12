#Number of islands
#https://leetcode.com/problems/number-of-islands/description/

class BFS(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.memory = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]

    def isValid(self,row, col):
        #if row and col are in bounds
        if(row >= 0 and row < len(self.matrix) and col >= 0 and col < len(self.matrix[0])):
            # and if they have not been seen before and is one
            if(self.matrix[row][col] == 1 and self.memory[row][col] == 0):
                return True
        return False

    def count(self, queue):
        while queue:
            top = queue.pop(0)
            row = top[0]
            col = top[1]
            #mark in in memory
            self.memory[row][col] = 1
            #up
            if(self.isValid(row-1, col)):
                queue.append([row-1, col])
            #down
            if(self.isValid(row+1, col)):
                queue.append([row+1, col])
            #left
            if(self.isValid(row, col-1)):
                queue.append([row, col-1])
            #right
            if(self.isValid(row, col+1)):
                queue.append([row, col+1])

    def solution(self):
        islandCount = 0
        #start going through matrix
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                #if we have not seen the cell before and its one 
                if(self.matrix[row][col] == 1 and self.memory[row][col] == 0):
                    #this can be start of an island
                    islandCount = islandCount + 1
                    self.count([[row, col]])
        print islandCount
        print "you can do this inplace by using input matrix as memory"
        print "by setting cell's that are visited as 0"


#Main
m = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
o = BFS(m)
o.solution()
