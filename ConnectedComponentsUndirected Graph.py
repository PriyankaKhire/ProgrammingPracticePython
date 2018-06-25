#Number of Connected Components in an Undirected Graph
#Difficulty:Medium
#
#Given n nodes labeled from 0 to n - 1 and a list of 
#undirected edges (each edge is a pair of nodes), 
#write a function to find the number of connected components in an undirected graph.
#
#Example 1:
#
#Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
#     0            3
#     |             |
#     1 --- 2    4 
#
#Output: 2
#Example 2:
#
#Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
#     0              4
#     |               |
#     1 --- 2 --- 3
#
#Output:  1
#Note:
#You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.


class UnDirectedGraph(object):
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.visited = []
        self.matrix = self.createMatrix()

    def createMatrix(self):
        matrix = [[0 for row in range(self.n)] for col in range(self.n)]
        for edge in self.edges:
            #edge is [a, b] so there is edge between a and b            
            e1 = edge[0]
            e2 = edge[1]
            matrix[e1][e2] = 1
            matrix[e2][e1] = 1
        return matrix

    def dfs(self, e):
        for edge in range(self.n):
            if(self.matrix[e][edge] == 1 and not(edge in self.visited)):
                self.visited.append(edge)
                self.dfs(edge)

    def solution(self):
        output = 0
        for edge in range(self.n):
            if not edge in self.visited:
                self.visited.append(edge)
                output = output +1
                self.dfs(edge)
                #print self.visited
        print output
        


#Main Program
o = UnDirectedGraph(5, [[0, 1], [1, 2], [3, 4]])
o.solution()
        
