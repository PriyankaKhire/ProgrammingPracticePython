#All Paths in a Directed Acyclic Graph from a source vertex to dest vertex
#this answer can be modified to calculate longest path between 2 vertices

def addEdge(i,j, weight):
    global graph
    graph[i][j] = weight

def isSafe(sourceVertex, curVertex, visited):
    #If there is an edge between the 2 vertices
    if(graph[sourceVertex][curVertex] != 0):
        #If this vertex has not been visited before
        if not curVertex in visited:
            return True
    return False

#Backtracking solution
def foo(sourceVertex, destVertex, path, length, weight):
    global graph
    if(sourceVertex == destVertex):
        print "path="+str(path)
        print "length="+str(length)
        print "weight="+str(weight)
        return
    for vertex in range(6):
        if(isSafe(sourceVertex, vertex, path)):
            path.append(vertex)
            foo(vertex, destVertex, path, length+1, weight+graph[sourceVertex][vertex])
            path.pop()

#Main Program
graph = [[0 for i in range(6)] for j in range(6)]
addEdge(0, 1, 5)
addEdge(0, 2, 3)
addEdge(1, 3, 6)
addEdge(1, 2, 2)
addEdge(2, 4, 4)
addEdge(2, 5, 2)
addEdge(2, 3, 7)
addEdge(3, 5, 1)
addEdge(3, 4, -1)
addEdge(4, 5, -2)

foo(0, 5, [0], 1, 0)
