#Fibonacci sequence
class Solution(object):
    def __init__(self, n):
        self.n = n

    def recurrsiveFibo(self, n):
        if(n == 0 or n == 1):
            return 1
        return self.recurrsiveFibo(n-1) + self.recurrsiveFibo(n-2)

    def iterativeFibo(self):
        prev = 0
        curr = 1
        for i in range(self.n):
            nxt = prev + curr
            prev = curr
            curr = nxt
        return curr
    
    def logic(self):
        #this one is fast
        print self.iterativeFibo()
        #its slow
        print self.recurrsiveFibo(self.n)
        

#Main
obj = Solution(35)
obj.logic()
