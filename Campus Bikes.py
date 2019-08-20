# Campus Bikes
# https://leetcode.com/problems/campus-bikes/
import heapq
class BikeWorkerRelation(object):
    def __init__(self, bI, wI):
        self.bI = bI
        self.wI = wI
        self.manhattanDistance = None
        
class Solution(object):
    def __init__(self):
        self.bikeHash = {}
        self.workerHash = {}
    
    def calculateManhattanDistance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def createBikeWorkerRelation(self, worker, bike, wI, bI):
        obj = BikeWorkerRelation(bI, wI)
        obj.manhattanDistance = self.calculateManhattanDistance(bike, worker)
        return obj

    def popFromHeap(self, heap, bikes):
        answer = [None for i in range(len(bikes))]
        while(heap):
            top = heapq.heappop(heap)
            obj = top[1]
            # if both worker and bike have not been takent then assign them to each other
            if(self.workerHash[obj.wI] == None and self.bikeHash[obj.bI] == None):
                self.workerHash[obj.wI] = True
                self.bikeHash[obj.bI] = True
                answer[obj.bI] = obj.wI
        return answer
    
    def assignBikes(self, workers, bikes):
        heap = []
        for wI in range(len(workers)):
            for bI in range(len(bikes)):
                obj = self.createBikeWorkerRelation(workers[wI], bikes[bI], wI, bI)
                # push the objects in heap with respect to manhatten distance.
                heapq.heappush(heap, (obj.manhattanDistance, obj))
        # we keep track if a bike or a worker has been assigned to each other or not.
        # by default non have been assigned to each other yet.
        self.workerHash = {w:None for w in range(len(workers))}
        self.bikeHash = {b:None for b in range(len(bikes))}
        #finally we pop from heap and assign each bike to each worker
        print self.popFromHeap(heap, bikes)
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
# Main
workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]

workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
obj = Solution()
obj.assignBikes(workers, bikes)
