class Solution(object):
    
    def logic(self, combination):
        print combination
        # accessing elements in reverse order coz we wanna print 001 instead of 100
        for i in range(len(combination)-1, -1, -1):
            if (combination[i] != 1):
                combination[i] = 1
                self.logic(combination)
                combination[i] = 0

    def generateBinary(self, n):
        combination = [0 for i in range(n)]
        self.logic(combination)

# Main
obj = Solution()
obj.generateBinary(2)
