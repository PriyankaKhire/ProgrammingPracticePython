#Integer Break
#https://leetcode.com/problems/integer-break/description/


class IntegerBreak(object):
    def __init__(self, n):
        self.n = n
        self.outputs = []

    def product(self, array):
        p = 1
        for element in array:
            p = element*p
        return p
            
    def breakInteger(self, output, ones):
        #print ones, output
        if sum(output) == self.n:
            if not (sorted(output) in self.outputs):
                self.outputs.append(sorted(output))
            return
        for i in range(1, self.n):
            if((sum(ones) - i) >= 0):
                output.append(i)
                self.breakInteger(output, ones[i:])
                output.pop()

    def solution(self):
        ones = [1 for i in range(self.n)]
        self.breakInteger([], ones)
        #find the largest product
        for output in  self.outputs:
            print output,
            print " = ",
            print self.product(output)
                
        

#Main Program
o = IntegerBreak(10)
o.solution()
