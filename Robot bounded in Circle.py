# Robot Bounded In Circle
# https://leetcode.com/problems/robot-bounded-in-circle/
class Direction(object):
    def goNorth(self, x, y):
        return x, y+1
    
    def goSouth(self, x, y):
        return x,y-1
    
    def goWest(self, x, y):
        return x-1, y
    
    def goEast(self, x, y):
        return x+1, y
    
class Solution(object):
    def turnLeft(self, currDir):
        leftTurn = {
            'N':'W',
            'W':'S',
            'S':'E',
            'E':'N'
        }
        return leftTurn[currDir]
    
    def turnRight(self, currDir):
        rightTurn = {
            'N':'E',
            'E':'S',
            'S':'W',
            'W':'N'
        }
        return rightTurn[currDir]
    
    def go(self, currDir, x, y):
        print "Going", currDir
        direction = Direction()
        if (currDir == 'N'):
            return direction.goNorth(x, y)
        if (currDir == 'E'):
            return direction.goEast(x, y)
        if (currDir == 'S'):
            return direction.goSouth(x, y)
        if (currDir == 'W'):
            return direction.goWest(x, y)
    
    def isRobotBounded(self, instructions):
        x, y = 0, 0
        currDir = 'N'
        for instruction in list(instructions):
            print instruction, x, y, currDir
            if (instruction == 'G'):
                x, y = self.go(currDir, x, y)
            elif (instruction == 'L'):
                currDir = self.turnLeft(currDir)
                print "Going left, new dir", currDir
            elif (instruction == 'R'):
                currDir = self.turnRight(currDir)
                print "Going right, new dir", currDir
        if ((x == 0 and y == 0) or (currDir != 'N')):
            return True
        return False
        """
        :type instructions: str
        :rtype: bool
        """
        
