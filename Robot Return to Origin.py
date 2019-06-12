# Robot Return to Origin
#https://leetcode.com/problems/robot-return-to-origin/
class Solution(object):
    def judgeCircle(self, moves):
        position = [0,0]
        for move in moves:
            if(move == 'L'):
                position[1] = position[1] + 1
            elif(move == 'R'):
                position[1] = position[1] - 1
            elif(move == 'D'):
                position[0] = position[0] + 1
            elif(move == 'U'):
                position[0] = position[0] - 1
        if(position == [0,0]):
            return True
        return False
            
        """
        :type moves: str
        :rtype: bool
        """
#Main
obj = Solution()
print obj.judgeCircle("LLDDRRUU")
