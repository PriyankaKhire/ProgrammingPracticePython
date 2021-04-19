# Maximum Performance of a Team
# https://leetcode.com/problems/maximum-performance-of-a-team/
import heapq
class Employee(object):
    def __init__(self, speed, efficiency):
        self.speed = speed
        self.efficiency = efficiency
    
    # this is for heap insert
    def __cmp__(self, otherObject):
        return cmp(self.speed, otherObject.speed)
        
class Solution(object):
    def createEmployeeObjects(self, speed, efficiency):
        employeeObjects = []
        for i in range(len(speed)):
            obj = Employee(speed[i], efficiency[i])
            employeeObjects.append(obj)
        return employeeObjects
    
    def logic(self, speed, efficiency, k):
        employeeObjects = self.createEmployeeObjects(speed, efficiency)
        heap = []
        speedSum = 0
        performance = 0
        # first sort on efficiency in descending order.
        for employeeObject in sorted(employeeObjects, key=lambda x:x.efficiency, reverse=1):
            print "Current speed", employeeObject.speed, "Current efficiency", employeeObject.efficiency
            # if the heap is of size k
            if (len(heap) == k):
                print "Heap became of size k, so popping element"
                topObject = heapq.heappop(heap)
                speedSum = speedSum - topObject.speed
                print "Popped object with speed",topObject.speed, "efficiency", topObject.efficiency, "the current speed sum", speedSum
            # insert current object in heap
            # we are sorting this heap on basis of speed. see the __cmp__ method in above class
            heapq.heappush(heap, employeeObject)
            speedSum = speedSum + employeeObject.speed
            # since efficiency is sorted in descending order, our current efficiency is min efficiency already
            currentPerformance = speedSum*employeeObject.efficiency
            performance = max(performance, currentPerformance)
            print "Inserted current item in heap, total speed sum", speedSum, "current performance", currentPerformance, "total performance",performance
        return performance
            
    def maxPerformance(self, n, speed, efficiency, k):
        return self.logic(speed, efficiency, k)
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        
