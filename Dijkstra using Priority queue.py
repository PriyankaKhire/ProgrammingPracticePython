# Dijkastra with priority queue
import heapq
class Vertex(object):
    def __init__(self, vertex):
        self.name = vertex
        self.cost = float("inf")
        self.visited = False

    # helps us compare on object cost.
    def __cmp__(self, other):
        return cmp(self.cost, other.cost)
        
class Dijkstra(object):
    def __init__(self):
        self.matrix = None
        #key = vertex name, value = Vertex object
        self.vertices = {}
        # min heap sorted according to cost of vertices
        self.heap = []

    def logic(self, dst):
        # get the vertex with lowest cost
        vertexObj = heapq.heappop(self.heap)
        print "Currently processing vertex",vertexObj.name,"with cost",vertexObj.cost
        # mark it visited
        vertexObj.visited = True
        if(vertexObj.name == dst):
            print vertexObj.cost
            return
        # get all the unvisited neighbors of our current vertex
        for neighbor in range(len(self.matrix)):
            if(self.vertices[neighbor].visited == False and self.matrix[vertexObj.name][neighbor] != 0):
                # update their cost
                self.vertices[neighbor].cost = min(self.vertices[neighbor].cost, vertexObj.cost+self.matrix[vertexObj.name][neighbor])
                # heapify the heap
                heapq.heapify(self.heap)
        self.logic(dst)

    def fillVerticesHash(self,n):
        # create vertex object for each vertex and put it in vertex hash
        for vertex in range(n):
            self.vertices[vertex] = Vertex(vertex)

    def fillMatrix(self, paths):
        for path in paths:
            self.matrix[path[0]][path[1]] = path[2]
            self.matrix[path[1]][path[0]] = path[2]
        
    def findCheapestPath(self, paths, n, src, dst):
        self.matrix = [[0 for col in range(n)] for row in range(n)]
        self.fillMatrix(paths)
        self.fillVerticesHash(n)
        # make this src vertex cost as 0
        self.vertices[src].cost = 0
        # insert all vertices in heap
        for v in range(n):
            heapq.heappush(self.heap, self.vertices[v])
        self.logic(dst)

# Main
# first entry is src, second entry is dst and third entry is cost
n = 9
paths = [
    [0, 1, 4], # there is edge between 0 and 1 with cost 4
    [0,7, 8],
    [1, 7,11],
    [1, 2,8],
    [2, 3, 7],
    [2, 8, 2],
    [3,4, 9],
    [3,5, 14],
    [4, 5, 10],
    [5, 2, 4],
    [5, 6, 2],
    [6, 8, 6],
    [6, 7, 1],
    [7, 8, 7]
    ]
obj = Dijkstra()
obj.findCheapestPath(paths, n, 0, 4)
