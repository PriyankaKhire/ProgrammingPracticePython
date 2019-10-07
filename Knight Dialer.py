# Knight Dialer
# https://leetcode.com/problems/knight-dialer/
# took some help to understand meaning of problem form this article
# https://leetcode.com/problems/knight-dialer/discuss/190787/How-to-solve-this-problem-explained-for-noobs!!!
class Solution(object):
    def __init__(self):
        self.dialPad = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            ['*',0,'*']
            ]
        
    def isValid(self, row, col):
        if(row >= 0 and row < len(self.dialPad)):
            if(col >= 0 and col < len(self.dialPad[0])):
                if(self.dialPad[row][col] != '*'):
                    return True
        return False
        
    def backtrack(self, n, row, col, combination):
        print "number of hops remaining",n
        if(self.dialPad[row][col] == '*'):
            return 0
        if(n == 0):
            print "number dialed",combination
            return 1
        moves = [[-1, -2], [-1, 2], [-2, -1], [-2, 1], [1, -2], [1, 2], [2, -1], [2, 1]]
        totalMoves = 0
        for move in moves:
            new_r = row + move[0]
            new_c = col + move[1]
            if(self.isValid(new_r, new_c)):
                print "next key", self.dialPad[new_r][new_c]
                totalMoves = totalMoves + self.backtrack(n-1, new_r, new_c, combination+str(self.dialPad[new_r][new_c]))
        return totalMoves
                
    def knightDialer(self, N):
        total = 0
        for r in range(len(self.dialPad)):
            for c in range(len(self.dialPad[0])):
                print "Currently at key",self.dialPad[r][c]
                totalCombinationsDialed = self.backtrack(N-1, r, c, str(self.dialPad[r][c]))
                print "Total combinations of numbered dialed",totalCombinationsDialed,"\n"
                total = total + totalCombinationsDialed
        print total
        """
        :type N: int
        :rtype: int
        """
# Main
obj = Solution()
obj.knightDialer(3)
