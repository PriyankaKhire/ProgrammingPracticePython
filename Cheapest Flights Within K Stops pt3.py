class DFS(object):
    def __init__(self):
        self.matrix = None
        self.pathWithLeastCost = None
        self.leastCost = float("inf")

    def logic(self, dst, k, src, path, cost):
        if(len(path) > k+2):
            return
        # if src is dst then we print the path
        if(src == dst):
            if(self.leastCost > cost):
                self.pathWithLeastCost = path[:]
                self.leastCost = cost
            return
        # find all unvisited neighbors of src
        for n in range(len(self.matrix)):
            if(not(n in path) and self.matrix[src][n] != 0):
                self.logic(dst, k, n, path+[n], cost+self.matrix[src][n])

    def fillMatrix(self, flights, n):
        self.matrix = [[0 for col in range(n)] for row in range(n)]
        for src, dst, cost in flights:
            self.matrix[src][dst] = cost
        
    def findCheapestPrice(self, n, flights, src, dst, K):
        self.fillMatrix(flights, n)
        self.logic(dst, K, src, [src], 0)
        print self.pathWithLeastCost, self.leastCost

class Path(object):
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost
        
class BFS(object):
    def __init__(self):
        self.matrix = None
        self.lowestCostPathTillNow = float("inf")

    def logic(self, queue, dst, k):
        while(queue):
            top = queue.pop(0)
            # we dont wanna go beyond k+1 length paths
            if(len(top.path) > k+2):
                continue
            currNode = top.path[-1]
            if(currNode == dst):
                print top.path, top.cost
                # record the lowest cost,
                #this indicates, that if we try to find a path that has cost higher than already recorded lowest cost,
                #we dont proceed on that path.
                self.lowestCostPathTillNow = min(top.cost, self.lowestCostPathTillNow)
                continue
            # get all unvisited neighbors of currNode that have cost less than self.lowestCostPathTillNow
            for n in range(len(self.matrix)):
                if(not(n in top.path) and self.matrix[currNode][n] != 0 and self.lowestCostPathTillNow > top.cost+self.matrix[currNode][n]):
                    queue.append(Path(top.path + [n], top.cost+self.matrix[currNode][n]))

    def fillMatrix(self, flights, n):
        self.matrix = [[0 for col in range(n)] for row in range(n)]
        for src, dst, cost in flights:
            self.matrix[src][dst] = cost

    def findCheapestPrice(self, n, flights, src, dst, K):
        self.fillMatrix(flights, n)
        self.logic([Path([src], 0)], dst, K)
        if(self.lowestCostPathTillNow != float("inf")):
            print self.lowestCostPathTillNow
        else:
            print -1
    

# Main
dfs = DFS()
print "Test Case 1"
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
#dfs.findCheapestPrice(n, edges, src, dst, k)
bfs = BFS()
bfs.findCheapestPrice(n, edges, src, dst, k)
print "Test Case 2"
n = 4
edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
#dfs.findCheapestPrice(n, edges, src, dst, k)
bfs = BFS()
bfs.findCheapestPrice(n, edges, src, dst, k)
print "Test Case 3"
n = 17
edges = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
src = 13
dst = 4
k = 13
#dfs.findCheapestPrice(n, edges, src, dst, k) # takes too long
bfs = BFS()
bfs.findCheapestPrice(n, edges, src, dst, k)
