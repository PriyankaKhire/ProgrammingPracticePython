# Topological Sort using graph represented as a matrix
'''
Graph:
 0           ---> 5
            /       |
          /        \/
 1---->4------->6
 |       |
\/      |                
 2<----|
  |
 \/
  3
Matrix:
  0  1  2  3  4  5  6
0 0  0  0  0  0  0  0
1 0  0  1  0  1  0  0
2 0  0  0  1  0  0  0
3 0  0  0  0  0  0  0
4 0  0  1  0  0  1  1
5 0  0  0  0  0  0  1
6 0  0  0  0  0  0  0
'''

class CreateGraph(object):
    def __init__(self, height, width):
        self.matrix = [[0 for col in range(width)] for row in range(height)]

    def addLink(self, i, j):
        self.matrix[i][j] = 1

    def display(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                print self.matrix[row][col],
            print ""
        print ""

class Sorting(object):
    def __init__(self):
        self.graph = None

    def createGraph(self, height, width, connections):
        self.graph = CreateGraph(height, width)
        for link in connections:
            self.graph.addLink(link[0], link[1])
        self.graph.display()

    def dfs(self, matrix, currNode, stack):
        # if current node is already in the stack that means it's already been explored
        if (currNode in stack):
            return 
        # visit all childrens of the current node
        for child in range(len(matrix[0])):
            if (matrix[currNode][child] == 1):
                # we go in DFS and explore the child
                self.dfs(matrix, child, stack)
        # When all kids of the current node are explored we put it in stack
        stack.append(currNode)

    def logic(self):
        stack = []
        # Start exploring all nodes one by one
        for node in range(len(self.graph.matrix)):
            # if node has not already been visited then visit it
            if node in stack:
                continue
            self.dfs(self.graph.matrix, node, stack)
        # Pop the stack and we have the answer.
        stack.reverse()
        print stack


# Main
obj = Sorting()
obj.createGraph(7, 7, [[1, 2], [1, 4], [2, 3], [4, 2], [4, 5], [4, 6], [5, 6]])
obj.logic()
        
        
        
