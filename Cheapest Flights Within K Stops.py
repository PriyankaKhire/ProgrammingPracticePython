#Cheapest Flights Within K Stops
#https://leetcode.com/problems/cheapest-flights-within-k-stops/
class Solution(object):
    def __init__(self):
        self.matrix = None
        self.paths = []
        
    def createGraphMatrix(self, flights, n):
        self.matrix = [[-1 for col in range(n)] for row in range(n)]
        for flight in flights:
            src = flight[0]
            dst = flight[1]
            price = flight[2]
            self.matrix[src][dst] = price

    def bfs(self, queue, dst, k):
        print "Queue is ", queue
        if not queue:
            return
        top = queue.pop(0)
        src = top[0]
        price = top[1]
        moveNumber = top[2]
        visited = top[3][:]
        visited.append(src)
        print "Current node is ", src, " total price to reach dest is ", price, " move number ",moveNumber, " visited ", visited
        if(moveNumber <= k):
            if(src == dst):
                self.paths.append(price)
            else:
                for destination in range(len(self.matrix)):
                    if(self.matrix[src][destination] != -1 and not(destination in top[3])):
                        queue.append([destination, price+self.matrix[src][destination], moveNumber+1, visited])
        self.bfs(queue, dst, k)
        
    def findCheapestPrice(self, n, flights, src, dst, K):
        self.createGraphMatrix(flights, n)
        self.bfs([[src, 0, -1, []]], dst, K)
        if not (self.paths):
            print -1
            return
        print min(self.paths)
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
#Main
'''
obj1 = Solution()
obj1.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)

obj2 = Solution()
obj2.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)

obj3 = Solution()
obj3.findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1)
'''
obj4 = Solution()
obj4.findCheapestPrice(5, [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]], 0, 2, 2)
