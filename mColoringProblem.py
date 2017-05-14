#m Coloring Problem

#Given an undirected graph and a number m,
#determine if the graph can be colored with at most m colors such that no two adjacent vertices
#of the graph are colored with same color. Here coloring of a graph means assignment of colors to
#all vertices.

#Input:
#1) A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V] is
#adjacency matrix representation of the graph. A value graph[i][j] is 1 if there is a direct
#edge from i to j, otherwise graph[i][j] is 0.
#2) An integer m which is maximum number of colors that can be used.

#Output:
#An array color[V] that should have numbers from 1 to m. colour[i] should represent the
#color assigned to the ith vertex. The code should also return false if the graph cannot be
#colored with m colors.

#Global variables
v = 4
m = 3
colour = [-1 for i in range(v)]

def isSafeColor(color, vertex, graph):
    for col in range(v):
        if(graph[vertex][col] == 1 and colour[col] == color):
            return False
    return True
    
def foo(vertex, graph, m):
    #Return condition
    if(vertex == v):
        print "\n\n colour matrix "+str(colour)
        return True
    print "Vertex = "+str(vertex)
    for color in range(m):
        print "Color = "+str(color)
        print "is Safe ? "+str(isSafeColor(color, vertex, graph))
        #For vertex v inside graph g is color m safe ?
        if(isSafeColor(color, vertex, graph)):
            colour[vertex] = color
            print "colour matrix "+str(colour)
            if(foo(vertex+1, graph, m)):
                return True
            else:
                print "*** Back Tracking ***"
                colour[vertex] = -1

#Main program
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
    ]

foo(0, graph, m)

                
