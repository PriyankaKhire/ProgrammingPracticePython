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

    def dpFibo(self):
        #Adding +2 because for some reason it was skipping the last 2
        f = [0 for i in range(self.n+2)]
        f[0] = 0
        f[1] = 1
        for i in range(2, self.n+2):
            f[i] = f[i-1]+f[i-2]
        return f
    
    def logic(self):
        #this one is fast
        print self.iterativeFibo()
        #dp fibo
        print self.dpFibo()
        #its slow
        print self.recurrsiveFibo(self.n)
        

#Main
obj = Solution(35)
obj.logic()
