#Find if there is a path of more than k length from a source

#Given a graph, a source vertex in the graph and a number k, find if there is a simple path
#(without any cycle) starting from given source and ending at any other vertex.

#Input:
#A 2D array where if there exists an edge between vertex i and j then it is denoted by the
# weight between them
#if there is no edge between j and i then it is indicated by -1

'''
Hint: they say without any cycle so this means if a vertex has already been visited then dont visit it again
'''
def isSafe(curEdge, edge, solution):
    #If there is an edge between curEdge and edge
    if(graph[curEdge][edge] > -1):
        #and if that edge is not visited
        if not(edge in solution):
            return True
    return False

def foo(curSum, curEdge, solution, k):
    global v
    global graph
    if curSum >= k:
        print solution
        print curSum
        #If you return true then it will only print one path
        return True
        #If you just return and not return true then it will print all paths,
        #try it and see by uncommenting this return and commenting this return True
        #return
    for edge in range(v):
        #If edge is safe
        if(isSafe(curEdge, edge, solution)):
            solution.append(edge)
            if(foo(curSum+graph[curEdge][edge], edge, solution, k)):
                return True
            else:
                #backtrack
                solution.pop()
            
    

def addEdge(i,j, weight):
    global graph
    graph[i][j] = weight
    graph[j][i] = weight

#Main program
v = 9
graph = [[-1 for i in range(v)] for j in range(v)]
addEdge(0, 1, 4)
addEdge(0, 7, 8)
addEdge(1, 2, 8)
addEdge(1, 7, 11)
addEdge(2, 3, 7)
addEdge(2, 8, 2)
addEdge(2, 5, 4)
addEdge(3, 4, 9)
addEdge(3, 5, 14)
addEdge(4, 5, 10)
addEdge(5, 6, 2)
addEdge(6, 7, 1)
addEdge(6, 8, 6)
addEdge(7, 8, 7)
#for i in range(v):
    #print graph[i]

print foo(0, 0, [0], 58)
print foo(0, 0, [0], 62)
