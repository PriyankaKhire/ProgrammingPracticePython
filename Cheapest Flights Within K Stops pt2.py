# Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import heapq
class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.cost = float("inf")
        self.path = []
        self.visited = False

    def __cmp__(self, other):
        return cmp(self.cost, other.cost)
    
class Solution(object):
    def __init__(self):
        # key = vertex, value = object
        self.vertices = {}
        # graph matrix
        self.matrix = None
        # min heap sorted according to cost
        self.heap = []

    def logic(self, dst, k):
        # get the vertex at the top of heap
        currVertex = heapq.heappop(self.heap)
        # mark current vertex visited
        currVertex.visited = True
        print "Current vertex is",currVertex.name, "with cost",currVertex.cost,"with Path",currVertex.path
        # if its destination then print cost and return
        if(currVertex.name == dst):
            print currVertex.cost, currVertex.path
            return
        # get all unvisited neighbors of current vertex
        for n in range(len(self.vertices)):
            if(self.vertices[n].visited == False and self.matrix[currVertex.name][n] != 0):
                # if the current vertex cost + cost of path between current vertex and neighbor is less than the cost of neighbor
                if(currVertex.cost+self.matrix[currVertex.name][n] < self.vertices[n].cost):
                    # if path length is less than or equal to k+1
                    # why k+1 ? coz k is number of allowed stops between src and dst and path includes src
                    if(not self.vertices[n].path or len(currVertex.path+[currVertex.name]) <= k+1):
                        # update the cost
                        self.vertices[n].cost = currVertex.cost+self.matrix[currVertex.name][n]
                        # update the path
                        self.vertices[n].path = currVertex.path+[currVertex.name]
                        # heapify the heap
                        heapq.heapify(self.heap)
        self.logic(dst, k)
        
    def fillVerticesHash(self, n):
        for v in range(n):
            self.vertices[v] = Vertex(v)

    def createGraphMatrix(self, flights, n):
        self.matrix = [[0 for col in range(n)] for row in range(n)]
        for path in flights:
            self.matrix[path[0]][path[1]] = path[2]
            
    def findCheapestPrice(self, n, flights, src, dst, K):
        self.fillVerticesHash(n)
        self.createGraphMatrix(flights, n)
        # change the cost of src vertex to 0 so its at the top of heap
        self.vertices[src].cost = 0
        # add all vertices in heap
        for v in range(n):
            heapq.heappush(self.heap, self.vertices[v])
        self.logic(dst, K)
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        

# Main
edges = [[0,1,100],[1,2,100],[0,2,500]]
obj = Solution()
#obj.findCheapestPrice(3, edges, 0, 2, 0)
#obj.findCheapestPrice(3, edges, 0, 2, 1)

n = 17
edges = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
src = 13
dest = 4
k = 13
obj.findCheapestPrice(n, edges, src, dest, k)

n = 4
edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dest = 3
k = 1
obj.findCheapestPrice(n, edges, src, dest, k)
