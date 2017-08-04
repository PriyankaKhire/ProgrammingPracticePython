#DFS

class stack():
    def __init__(self):
        self.array = []
    def push(self, data):
        self.array.append(data)
    def pop(self):
        del self.array[-1]
    def top(self):
        return self.array[-1]

def dfs(s, m, r, v):
    #if stack not empty
    if s:
        t = s.top()
        #If the element not visited
        if v[t] == 0:
            #mark it as visited
            v[t] = 1
            #Add it to the result
            r.append(t)
            #Get the first unvisited adjacent element
            for adjacentElement in range(9):
                if(m[t][adjacentElement] == 1 and v[adjacentElement] == 0):
                    #Push it on top of the stack
                    s.push(adjacentElement)
                    dfs(s,m,r,v)
        s.pop()
    return r

def foo(m):
    s = stack()
    visited = [0 for col in range(9)]
    s.push(0)
    result = dfs(s, m, [], visited)
    print result
    
    

#Main Program
matrix = [[0 for col in range(9)] for row in range(9)]
matrix[0][1] = 1
matrix[0][8] = 1
matrix[1][0] = 1
matrix[8][0] = 1
matrix[8][2] = 1
matrix[8][6] = 1
matrix[2][3] = 1
matrix[2][4] = 1
matrix[2][5] = 1
matrix[2][8] = 1
matrix[3][2] = 1
matrix[4][2] = 1
matrix[4][7] = 1
matrix[5][2] = 1
matrix[5][6] = 1
matrix[6][8] = 1
matrix[6][5] = 1
matrix[7][4] = 1
matrix[7][6] = 1
foo(matrix)
