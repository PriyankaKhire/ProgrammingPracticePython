#The maze
#https://leetcode.com/articles/the-maze/

#helper class that has some common functions
class helper(object):

    def __init__(self, inputMatrix, source, destination):
        self.inputMatrix = inputMatrix
        self.source = source
        self.destination = destination
        #Create output matrix of row and columns filled with 0s
        self.outputMatrix = [[0 for col in range(len(inputMatrix[0]))] for row in range(len(inputMatrix))]
        self.directions = ['up', 'down', 'left', 'right']

    #Gives all valid moves for the current move avoiding borders of matrix and walls
    def possibleMoves(self, currentMove):
        output = []
        dir_output = []
        row = currentMove[0]
        col = currentMove[1]
        #up
        r = row - 1
        #if row is within bounds of maze matrix
        if(r >= 0):
            #if there is no wall there in maze
            if(self.inputMatrix[r][col] == 0):
                output.append([r, col])
                dir_output.append("up")
        #down
        r = row +1
        #if row is within bounds of the maze
        if(r < len(self.inputMatrix)):
            #if there is no wall
            if(self.inputMatrix[r][col] == 0):
                output.append([r, col])
                dir_output.append("down")
        #right
        c = col +1
        if(c < len(self.inputMatrix[0])):
            if(self.inputMatrix[row][c] == 0):
                output.append([row, c])
                dir_output.append("right")
        #left
        c = col -1
        if(c >=0):
            if(self.inputMatrix[row][c]==0):
                output.append([row, c])
                dir_output.append("left")
        return output, dir_output

    #returns if current move is valid
    def isValidMove(self, move, nextMove):
        possible_moves, dirs = self.possibleMoves(move)
        if (nextMove in possible_moves):
            return True
        return False
    
    #rolls in the given direction until it hits a wall and returns cell where it stops
    def roll(self, direction, pos):
        row = pos[0]
        col = pos[1]
        if(direction == "left"):
            #col -1
            while(self.isValidMove([row, col], [row, col-1])):
                col = col -1
            return [row, col]
        if(direction == "right"):
            #col +1
            while(self.isValidMove([row, col], [row, col+1])):
                col = col +1
            return [row, col]
        if(direction == "up"):
            #row -1
            while(self.isValidMove([row, col], [row-1, col])):
                row = row -1
            return [row, col]
        if(direction == "down"):
            #row +1
            while(self.isValidMove([row, col], [row+1, col])):
                row = row +1
            return [row, col]

class dfs(helper):

    def __init__(self, inputMatrix, source, destination):
        helper.__init__(self, inputMatrix, source, destination)        

    def logic(self, src , dest, sol, om):
        if(src == dest):
            print "Found solution"
            print sol
            for row in range(len(om)):
                print om[row]
            return
        #print src, sol
        for d in self.directions:
            after_roll = self.roll(d, src)
            if(after_roll != src and om[after_roll[0]][after_roll[1]] == 0):
                om[after_roll[0]][after_roll[1]] = 1
                sol.append(d)
                self.logic(after_roll, dest, sol, om)
                #Backtracking
                sol.pop()
                om[after_roll[0]][after_roll[1]] = 0
                

    def solution(self):
        self.outputMatrix[self.source[0]][self.source[1]] = 1
        self.logic(self.source, self.destination, [], self.outputMatrix)

class bfsBase(object):

    def __init__(self, direction, row, col, parent):
        self.direction = direction
        self.row = row
        self.col = col
        self.parent = parent
        self.childern = []

#Here for bfs approach we design a tree with multiple childern and a queue
class bfs(helper):

    def __init__(self, inputMatrix, source, destination):
        helper.__init__(self, inputMatrix, source, destination)
        self.q = []

    def create_bfsBaseNode(self, row, col, direction, parent):
        node = bfsBase(direction, row, col, parent)
        return node
    
    def solution(self):
        #Create node for the source of the maze
        src_node = self.create_bfsBaseNode(self.source[0], self.source[1], "head", None)
        #Push that in queue
        self.q.append(src_node)
        #put 1 in output matrix
        self.outputMatrix[self.source[0]][self.source[1]] = 1
        possible_moves, possible_directions = self.possibleMoves([2,4])
        #correct the program where possible_moves are given after the roll
        '''
        #while q is not empty
        while(self.q):
            top = self.q.pop(0)
            #Get the possible directions
            possible_moves, possible_directions = self.possibleMoves([top.row, top.col])
            #put these moves in q
            for i in range(possible_moves):
                move = possible_moves[i]
                #if not previously visited before
                if(self.outputMatrix[move[0]][move[1]] == 0):
                    #Mark it visited
                    self.outputMatrix[move[0]][move[1]] = 1
                    #Create node for the move
                    node = create_bfsBaseNode(move[0], move[1], possible_directions[i], top)
                    #Add this node as top's childern
                    top.childern.append(node)
                    #Add it to queue
                    self.q.append(node)
                    '''
            
        
            

#Main Program
m = [[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0]]
s = [0,4]
d = [4,4]
#h = dfs(m,s,d)
#h.solution()

b = bfs(m,s,d)
b.solution()
