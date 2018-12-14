#House Robber
#https://leetcode.com/problems/house-robber/description/

class Solution(object):
    def __init__(self, houses):
        self.houses = houses

    def backtracking(self, index, output):
        if(index >= len(self.houses)):
            print "Houses robbed are ", output, " Value collected is ",sum(output)
            return 
        for i in range(index, len(self.houses)):
            output.append(self.houses[i])
            self.backtracking(i+2, output)
            output.pop()

    def logic(self):
        print "backtracking way"
        self.backtracking(0, [])

#Main
obj = Solution([5, 3, 4, 11, 2])
obj.logic()
