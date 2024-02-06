# Detecting a cycle in a graph
# We represent the graph in form of a matrix

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

class DetectCycles(object):
    def __init__(self):
        self.graph = None

    def createGraph(self, height, width, connections):
        self.graph = CreateGraph(height, width)
        for link in connections:
            self.graph.addLink(link[0], link[1])
        self.graph.display()

    def dfs(self, matrix, visited, node):
        print "At node", node, visited
        if (node in visited):
            return True
        # visit all childrens
        for child in range(len(matrix[0])):
            if (matrix[node][child] == 1):
                # visit that node
                visited.append(node)
                if (self.dfs(matrix, visited, child)):
                    # there is a cycle
                    return True
                # not a cycle
                return False
        # if node doesn't have and children
        visited.append(node)

    def logic(self):
        visited = []
        for node in range(len(self.graph.matrix)):
            if node not in visited:
                print "visiting node", node
                if (self.dfs(self.graph.matrix, visited, node)):
                    return True
        return False


# Main
obj = DetectCycles()
# for image of this graph, go here: https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
obj.createGraph(4, 4, [[0, 1], [0, 2], [1, 2], [2, 3], [2, 0]])
print obj.logic()
# for image of this graph, go here: https://workat.tech/problem-solving/practice/detect-cycle-in-directed-graph
obj.createGraph(7, 7, [[0,1], [0,3], [0,6], [1,2],[1,4],[4,5]])
print obj.logic()
# for image of this graph, go here: https://www.codingninjas.com/studio/problems/detect-cycle-in-     a-directed-graph_1062626
obj.createGraph(6, 6, [[0,1],[1,2],[2,3],[3,4], [3,5], [4,1]])
print obj.logic()    
        
