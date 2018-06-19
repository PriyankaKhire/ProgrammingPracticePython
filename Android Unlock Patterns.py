#Android Unlock Patterns
#
#Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.
#
#Rules for a valid pattern:
#Each pattern must connect at least m keys and at most n keys.
#All the keys must be distinct.
#If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
#The order of keys used matters.
#
#Explanation:
#| 1 | 2 | 3 |
#| 4 | 5 | 6 |
#| 7 | 8 | 9 |
#Invalid move: 4 - 1 - 3 - 6 
#Line 1 - 3 passes through key 2 which had not been selected in the pattern.
#
#Invalid move: 4 - 1 - 9 - 2
#Line 1 - 9 passes through key 5 which had not been selected in the pattern.
#
#Valid move: 2 - 4 - 1 - 3 - 6
#Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
#
#Valid move: 6 - 5 - 4 - 1 - 9 - 2
#Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
#
#Example:
#Given m = 1, n = 1, return 9.

class Solution(object):
    def __init__(self):
        self.keyPad = [[1,2,3],[4,5,6],[7,8,9]]
        self.directions = ["up", "down", "left", "right", "diagonal-up-left", "diagonal-up-right", "diagonal-down-left", "diagonal-down-right"]
        self.totalPatterns = 0
        
    def printCombination(self, combination):
        for i in range(len(combination)):
            r = combination[i][0]
            c = combination[i][1]
            print self.keyPad[r][c],
            print "->",
        print ""

        
    #gives next move based on direction 
    def nextMove(self, direction, row, col):
        if(direction == "up"):
            return row-1, col
        if(direction == "down"):
            return row+1, col
        if(direction == "left"):
            return row, col-1
        if(direction == "right"):
            return row, col+1
        if(direction == "diagonal-up-left"):
            return row-1, col-1
        if(direction == "diagonal-up-right"):
            return row-1, col+1
        if(direction == "diagonal-down-left"):
            return row+1, col-1
        if(direction == "diagonal-down-right"):
            return row+1, col+1

    #checks the bounds
    def checkBounds(self, row, col):
        if(row >= 0 and row < 3):
            if(col >=0 and col <3):
                return True
        return False
    
    #keys is the number of keys allowed to use
    def countPatterns(self, keys, row, col, combination):
        #return condition
        if(keys == len(combination)):
            self.totalPatterns = self.totalPatterns+1
            self.printCombination(combination)
            return
        #for every current key we have 9 moves
        for direction in self.directions:
            #Get next move
            n_row, n_col = self.nextMove(direction, row, col)
            #check bounds
            #check if its present in combination or not
            while(self.checkBounds(n_row, n_col) and ([n_row, n_col] in combination)):
                n_row, n_col = self.nextMove(direction, n_row, n_col)
            if(self.checkBounds(n_row, n_col)):
                #append this new row and col to combination
                combination.append([n_row, n_col])
                self.countPatterns(keys, n_row, n_col, combination)
                combination.pop()
            
        
    def numberOfPatterns(self, m, n):
        for key in range(m, n+1):
            for r in range(3):
                for c in range(3):
                    self.countPatterns(key, r, c, [[r,c]])
        print "Total Patterns = ",
        print self.totalPatterns

#MainProgram
o = Solution()
o.numberOfPatterns(1,3)

