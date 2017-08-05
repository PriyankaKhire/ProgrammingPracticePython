#Breadth first search
class queue():
    def __init__(self):
        self.array = []
    def push(self, data):
        self.array.append(data)
    def pop(self):
        if not self.array:
            return
        del self.array[0]
    def top(self):
        return self.array[0]
    def isEmpty(self):
        if not self.array:
            return True
        return False

def bfs(m, q, result, visited):
    #If q is not empty
    if not q.isEmpty():
        #Pop the top element
        t = q.top()
        q.pop()
        #Add it to result
        result.append(t)
        #Add all its adjacent unvisited elements to the q
        for adjacentElement in range(9):
            if(m[t][adjacentElement] == 1 and visited[adjacentElement] == 0):
                #Mark it visited
                visited[adjacentElement] = 1
                #Add it to the q
                q.push(adjacentElement)
        bfs(m, q, result, visited)
    return result

def foo(matrix):
    q = queue()
    q.push(0)
    v = [0 for col in range(9)]
    v[0] = 1
    r = bfs(matrix, q, [], v)
    print r

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
