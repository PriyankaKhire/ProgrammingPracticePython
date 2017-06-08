#Topological sort
#Basic idea:  only when all edges have been explored you add it in stack

def addEdge(i,j):
    global graph
    graph[i][j] = 1

def allVisited(vertex, visited, stack):
    global graph
    for i in range(8):
        if graph[vertex][i] == 1:
            if not (i in visited and i in stack):
                return False
    return True

def isSafe(curVertex, vertex, visited, stack):
    global graph
    #if there is an edge between curVertex and vertex
    if graph[curVertex][vertex] == 1:
        #if vertex has not been visited
        if not (vertex in visited):
            if not(vertex in stack):
                return True

def foo(curVertex):
    global graph, visited, stack
    print "current vertex "+str(curVertex)+" visited "+str(visited)+" stack "+str(stack)
    #if current vertex has all its childern explored
    print "All visited ?"+str(allVisited(curVertex, visited, stack))
    if (allVisited(curVertex, visited, stack)):
        print "Appending "+str(curVertex)+" to stack"
        return
    for vertex in range(8):
        print "for vertex "+str(curVertex)
        print "vertex "+str(vertex)+ " is safe ?"+str(isSafe(curVertex, vertex, visited, stack))
        if(isSafe(curVertex, vertex, visited, stack)):
            visited.append(vertex)
            foo(vertex)
            stack.append(visited.pop())
            print stack

#Main
graph = [[0 for i in range(8)] for j in range(8)]
addEdge(0,2)
addEdge(1,2)
addEdge(1,3)
addEdge(2,4)
addEdge(3,5)
addEdge(4,5)
addEdge(4,7)
addEdge(5,6)

visited = []
stack = []
for vertex in range(8):
    #if vertex is not visited then
    if not (vertex in visited and vertex in stack):
        print "visiting vertex "+str(vertex)
        visited.append(vertex)
        foo(vertex)
        if not vertex in stack:
            stack.append(vertex)

print "\n\n"
for num in range(8):
    print stack.pop()
