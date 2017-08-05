#Topological sort
#Only add virtices when all the adjacent vertices are explored
class stack():
    def __init__(self):
        self.array = []
    def push(self, data):
        self.array.append(data)
    def pop(self):
        if self.array:
            del self.array[-1]
    def top(self):
        return self.array[-1]
    def isEmpty(self):
        if not self.array:
            return True
        return False
    def display(self):
        return self.array

def topo(s,m, r, v):
    if not s.isEmpty():
        #Get the top element and visit it
        t = s.top()
        v[t] = 1
        print "Top element in stack is "+str(t)
        #Add all the unvisited adjacent elements to stack
        for adjacentElement in range(6):
            if(m[t][adjacentElement] == 1 and v[adjacentElement]==0):
                print "Pushing element "+str(adjacentElement)
                s.push(adjacentElement)
                print "Going in recurrssion"
                topo(s,m,r,v)
        r.append(t)
        s.pop()
        print "Result is "+str(r)
        print "Stack is "+str(s.display())
    return r,v

def foo(m):
    s = stack()
    visited = [0 for col in range(6)]
    result = []
    for element in range(6):
        if(visited[element] == 0):
            s.push(element)
            print "Pushing element "+str(element)+" in the stack"
            result, visited = topo(s, m, result, visited)
            print "Result so far is "+str(result)
            print "Visited so far is "+str(visited)
    #Reverse the result
    print result[::-1]



#Matrix
matrix = [[0 for col in range(6)] for row in range(6)]
matrix[2][3] = 1
matrix[3][1] = 1
matrix[4][0] = 1
matrix[4][1] = 1
matrix[5][0] = 1
matrix[5][2] = 1
foo(matrix)
