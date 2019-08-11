# Minimum Cost to Hire K Workers
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
from __future__ import division
class Worker(object):
    def __init__(self, w, q, wtoq):
        self.wage = w
        self.quality = q
        self.WtoQ = wtoq

class Solution(object):
    def __init__(self):
        self.workers = []
        self.minCost = 99999

    def populateWorkers(self, quality, wage):
        for worker in range(len(quality)):
            w = Worker(wage[worker], quality[worker], (wage[worker]/quality[worker]))
            self.workers.append(w)
        # sort according to WtoQ in ascending order
        self.workers.sort(key=lambda x:x.WtoQ)

            

    def greedy(self, k, selectedWorkers, totalCost):
        if(k == 0):
            print "*"*50
            print '* Total cost after selecting k workers is',totalCost,'*'
            print "*"*50
            self.minCost = min(self.minCost, totalCost)
            return
        for worker in self.workers:
            if(worker in selectedWorkers):
                continue
            # other workers should be paid according to our top worker's wage to quality ratio
            # if other worker's wage after calculating it with top worker's wageToQuality ratio,
            # is less than the min wage they charge, then we dont select that worker
            topWorker = selectedWorkers[0]
            print "Current worker in consideration with wage",worker.wage,"quality",worker.quality
            print "We can pay this worker",(topWorker.WtoQ*worker.quality)
            if((topWorker.WtoQ*worker.quality) >= worker.wage):
                print "We have selected this worker"
                self.greedy(k-1, selectedWorkers+[worker], totalCost+(topWorker.WtoQ*worker.quality))
        
    def mincostToHireWorkers(self, quality, wage, k):
        self.populateWorkers(quality, wage)
        for worker in self.workers:
            print "Selecting top worker as worker with wage",worker.wage, "worker quality",worker.quality,"one quality charge",worker.WtoQ
            self.greedy(k-1, [worker], worker.wage)
            print "=-"*50
        print "The total min cost is ",self.minCost
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
# Main
quality = [10,20,5]
wage = [70,50,30]
K = 2

quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
K = 3
obj = Solution()
obj.mincostToHireWorkers(quality, wage, K)
