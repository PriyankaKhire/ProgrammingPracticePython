#Coin Change
# https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

class coinChange(object):
    def __init__(self, N, S):
        self.N = N
        self.S = S

    def logic(self, N, S, n, output):
        if n == N:
            print output
            return
        for i in S:
            if(i+n <= N):
                output.append(i)
                self.logic(N, S, i+n, output)
                #Backtrack
                output.pop()

    def solution(self):
        self.logic(self.N, self.S, 0, [])

#Main Program
cc = coinChange(10, [2, 5, 3, 6])
cc.solution()

