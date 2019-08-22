# Robot Room Cleaner
# https://leetcode.com/problems/robot-room-cleaner/
'''
Ok so i am not solving the problem there, I m mostly coding for you to understand how backtracking works
The arrows in their solution are confusing. so here is me trying to explain.
This is just an example of how you'd backtrack from one cell. I dont have patience to code the real thing.
for better understanding, please draw this your self and see.
check this out for more understanding.
https://leetcode.com/problems/robot-room-cleaner/discuss/183753/simplest-to-understand-JavaScript-DFS-%2B-backtracking-(explanation)
'''
class Solution(object):
    def __init__(self):
        self.originRow = None
        self.originCol = None
        self.neighborCells = {'up':[-1,0], 'down':[1,0], 'left':[0,-1], 'right':[0,1]}

    def isValid(self, row, col, room):
        if(row >= 0 and row < len(room)):
            if(col >= 0 and col < len(room[0])):
                if(room[row][col] != 1 and room[row][col] != 'C'):
                    return True
        return False

    def calculateNewCellValue(self, row, col, direction):
        print "Calculation new cell values"
        print row, col
        print self.neighborCells[direction][0], self.neighborCells[direction][1]
        new_row = row + self.neighborCells[direction][0]
        new_col = col + self.neighborCells[direction][1]
        print "new row",new_row,"new col",new_col,"in direction",direction
        return new_row, new_col

    def dfs(self, room, row, col, direction):
        print "Currently on ",row, col, "in direction",direction
        print "Room looks like this"
        if(row == self.originRow and col == self.originCol):
            print "We have cleaned the entire room"
            return
        #clean current cell
        room[row][col] = 'C'
        for r in range(len(room)):
            print room[r]
        # try going in same direction to the next cell
        nRow, nCol = self.calculateNewCellValue(row, col, direction)
        if(self.isValid(nRow, nCol, room)):
            print "Going in the same direction",direction
            self.dfs(room, nRow, nCol, direction)
        print "Since the current direciton",direction,"didnt work out we try other directions"
        # go to a different direciton that not been visited and not been blocked
        for d in self.neighborCells:
            if(d != direction):
                nRow, nCol = self.calculateNewCellValue(row, col, d)
                if(self.isValid(nRow, nCol, room)):
                    self.dfs(room, nRow, nCol, d)
        print "backtracking from cell",row,col
        
    
    def cleanRoom(self, room):
        print "The position of the robot doenst matter, it can start from 0,0 or anywhere"
        print "For the purpose of this example we start from 1, 3"
        self.originRow = 1
        self.originCol = 3
        print "Here is how the room looks like -> 1 is the blocked cell and 0 is empty cell"
        for row in range(len(room)):
            print room[row]
        print "Now every time I clean a cell I'll mark it as C"
        print "In reality for the problem, you'd put clean cells in a hash"
        # clean the origin
        room[1][3] = 'C'
        self.dfs(room, 0, 3, 'up')


# Main
room = [[0 for col in range(8)] for row in range(5)]
#Block the cells
room[0][5] = 1
room[1][5] = 1
room[2][1] = 1
room[3][0] = 1
room[3][1] = 1
room[3][2] = 1
room[3][4] = 1
room[3][5] = 1
room[3][6] = 1
room[3][7] = 1

obj = Solution()
obj.cleanRoom(room)
