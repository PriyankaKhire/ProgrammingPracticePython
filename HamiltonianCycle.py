#Hamiltonian Cycle
#Input:
#A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V]
#is adjacency matrix representation of the graph. A value graph[i][j] is 1 if there is a direct
#edge from i to j, otherwise graph[i][j] is 0.
#Output:
#An array path[V] that should contain the Hamiltonian Path.
#path[i] should represent the ith vertex in the Hamiltonian Path.
#The code should also return false if there is no Hamiltonian Cycle in the graph.

#Global variables
v = 5
visited = [-1 for i in range(v)]
path = []

def isSafe(main_vertex, vertex, graph, root_vertex, vertices_covered):
    #To check if current vertex is root vertex
    if(graph[main_vertex][vertex] == 1 and vertex == root_vertex and vertices_covered == (v-1)):
        return True
    #if there is an edge between main vertex and the current vertex
    #and if the current vertex has not been explored
    if(graph[main_vertex][vertex] == 1 and visited[vertex] == -1):
        return True

def foo(graph, vertex, vertices_covered, root_vertex):
    #Return condition
    if (vertices_covered == v and vertex == root_vertex):
        print "\n The final path is "+str(path)
        return True
    print "Current Vertex = "+str(vertex)
    print "vertices covered = "+str(vertices_covered)
    for currV in range(v):
        print "for vertex "+str(currV)+" is safe ? "+str(isSafe(vertex, currV, graph, root_vertex, vertices_covered))
        if(isSafe(vertex, currV, graph, root_vertex, vertices_covered)):
            path.append(currV)
            visited[vertex] = 1
            print "path till now "+str(path)
            print "visited vertices "+str(visited)
            if(foo(graph, currV, vertices_covered+1, root_vertex)):
                return True
            else:
                path.pop()
                visited[vertex] = -1

#Main Program
'''
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
    ]
path.append(0)
print foo(graph, 0, 0, 0)
'''
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
    ]
path.append(0)
print foo(graph, 0, 0, 0)

