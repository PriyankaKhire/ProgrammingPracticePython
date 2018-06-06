#Coin Change
# https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

class coinChange(object):
    def __init__(self, N, S):
        self.N = N
        self.S = S

    def logic_approach2(self, N, S, n, output):
        if n == N:
            print output
            return
        for i in range(len(S)):
            if(S[i]+n <=N):
                output.append(S[i])
                self.logic_approach2(N, S, S[i]+n, output)
                #Backtrack
                output.pop()
            #Backtrack
            S.pop()

    def logic_approach1(self, N, S, n, output):
        if n == N:
            print output
            return
        for i in S:
            if(i+n <= N):
                output.append(i)
                self.logic_approach1(N, S, i+n, output)
                #Backtrack
                output.pop()

    def solution(self):
        self.logic_approach1(self.N, self.S, 0, [])
        print "-----------"
        self.logic_approach2(self.N, self.S, 0, [])

#Main Program
cc = coinChange(10, [2, 5, 3, 6])
cc.solution()

