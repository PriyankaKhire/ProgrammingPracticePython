# Dijkstra's Shortest Path Algorithm
# https://www.youtube.com/watch?v=pVfj6mxhdMw

class Dijkstras(object):
    def __init__(self):
        self.visited = None
        # key is the vertex and value is [cameFromVertex, pathCost]
        self.distances = {}

    def logic(self, currentVertex, graphMatrix, visitedVertices):
        if(visitedVertices == len(graphMatrix)):
            return
        for vertex in range(len(graphMatrix)):
            # if the vertex has not been visited and if ther is an edge between current vertex and vertex
            if(self.visited[vertex] == False and graphMatrix[currentVertex][vertex] != 0):
                if(self.distances[currentVertex][1] + graphMatrix[currentVertex][vertex] < self.distances[vertex][1]):
                    self.distances[vertex][1] = self.distances[currentVertex][1] + graphMatrix[currentVertex][vertex]
                    self.distances[vertex][0] = currentVertex
        self.visited[currentVertex] = True
        # find the next vertex with lowest cost that has not been visited, so that we can visit it next
        nextVertexToVisit = None
        lowestCost = float('inf')
        for vertex in self.distances:
            if(self.visited[vertex] == False and self.distances[vertex][1] < lowestCost):
                lowestCost = self.distances[vertex][1]
                nextVertexToVisit = vertex
        self.logic(nextVertexToVisit, graphMatrix, visitedVertices+1)
        
    
    def findShortestPath(self, originVertex, graphMatrix):
        # populating with default values.
        self.visited = [False for i in range(len(graphMatrix))]
        for vertex in range(len(graphMatrix)):
            self.distances[vertex] = [None, float("inf")]
        # cost of origin vertex is 0 and cameFromVertex is None
        self.distances[originVertex][1] = 0
        self.logic(originVertex, graphMatrix, 0)
        print "Thus the shortest path form origin vertex", originVertex, "to all other vertices is:\n",self.distances
        

# Main
graph = [
    [0, 6, 0, 1, 0],
    [6, 0, 5, 2, 2],
    [0, 5, 0, 0, 5],
    [1, 2, 0, 0, 1],
    [0, 2, 5, 1, 0]
    ]
obj = Dijkstras()
obj.findShortestPath(0, graph)
