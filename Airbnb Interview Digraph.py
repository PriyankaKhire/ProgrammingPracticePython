'''
Given a directed graph G (can contain sub graphs and cycles),
find the minimum number of vertices from which all nodes are reachable.

For example:

Nodes:
    0, 1, 2, 3, 4, 5

Edges:
    1 <- 0
    0 <- 1 <- 2
    3 <- 1 <- 2
    2 <- 5
    4 <- 5

Representation:
    --> 4
  /
 5 --> 2 --> 1 <--> 0
              \
                --> 3
Matrix:
g = [[1, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 1]]
Return 1 (node number 5). From node number 5 all other nodes are reachable.

If we remove edge 2 <- 5, the result is 2, because we need at least nodes number 5 and 2 to visit all nodes.

Representation of the graph if we remove the edge between nodes 2 and 5.

 5 --> 4

 2 --> 1 <--> 0
        \
          --> 3
'''
class Solution(object):
    def __init__(self):
        self.hash = {}
        self.pickedVertices = []
        self.visited = None

    def dfs(self, graph, vertex, visited, numberOfVisited):
        visited[vertex] = 1
        for i in range(len(graph[vertex])):
            if(graph[vertex][i] == 1 and i != vertex and visited[i] == 0):
                numberOfVisited[0] = numberOfVisited[0] +1
                self.dfs(graph, i, visited, numberOfVisited)

    def fillHash(self, graph):
        for vertex in range(len(graph)):
            self.visited = [0 for i in range(len(graph))]
            numberOfVisited = [1]
            self.dfs(graph, vertex, self.visited, numberOfVisited)
            # if at any time a vertex can visite all vertices return 1 since we are looking for number of vertices and not the vertex it self.
            if(numberOfVisited[0] == len(graph)):
                return 1
            self.hash[vertex] = [numberOfVisited[0], self.visited]
        return 0

    # if it coveres even one single vertex that has not been covered before then we return true
    def coversVerticesThatHaveNotBeenCoveredBefore(self, visitedByOtherVertex, visited):
        flag = False
        numberOfNewVerticesCovered = 0
        new_visited = visited[:]
        for i in range(len(visited)):
            if(visited[i] == 0 and visitedByOtherVertex[i] == 1):
                flag = True
                numberOfNewVerticesCovered = numberOfNewVerticesCovered + 1
                new_visited[i] = 1
        return flag, numberOfNewVerticesCovered, new_visited

    def findVertex(self, vertex, visited, numberOfCoveredVertices, vertexList, output):
        if(numberOfCoveredVertices == len(self.hash)):
            output.append(vertexList[:])
        for otherVertex in self.hash:
            if not(otherVertex in vertexList):
                flag, numberOfNewVerticesCovered, new_visited = self.coversVerticesThatHaveNotBeenCoveredBefore(self.hash[otherVertex][1], visited)
                if(flag):
                    vertexList.append(otherVertex)
                    self.findVertex(otherVertex, new_visited, numberOfCoveredVertices+numberOfNewVerticesCovered, vertexList, output)
                    vertexList.pop()
        

    def logic(self, graph):
        if(self.fillHash(graph) == 1):
            return 1
        minSet = None
        for vertex in self.hash:
            output = []
            self.findVertex(vertex, self.hash[vertex][1], self.hash[vertex][0], [vertex], output)
            # find list of vertices with min length
            for vertices in output:
                if(not minSet or len(minSet) > len(vertices)):
                    minSet = vertices
        return len(minSet)

#Main
'''
g1

    --> 4
  /
 5 --> 2 --> 1 <--> 0
              \
                --> 3
'''
g1 = [[1, 1, 0, 0, 0, 0],
     [1, 1, 0, 1, 0, 0],
     [0, 1, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 1, 0, 1, 1]]

'''
g2

 5 --> 4

 2 --> 1 <--> 0
        \
          --> 3
'''
g2 = [
    [1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1]
    ]

g3 = [[1, 0],
          [0, 1]]

g4 = [[1, 0],
          [1, 1]]

obj = Solution()
print obj.logic(g4)
