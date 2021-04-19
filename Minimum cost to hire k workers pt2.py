# Minimum Cost to Hire K Workers
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
class Worker(object):
    def __init__(self, wage, quality):
        self.wage = wage
        self.quality = quality
        
class Solution(object):
    def createWorkers(self, quality, wage):
        workers = []
        for i in range(len(quality)):
            obj = Worker(wage[i], quality[i])
            workers.append(obj)
        return workers
    
    def wageDetermination(self, mainWorker, workers):
        wages = []
        for worker in workers:
            # if current worker is not main worker then calculate other worker's wages.
            if not worker == mainWorker:
                # Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
                crossMultiplacationFormula = (mainWorker.wage*worker.quality)/float(mainWorker.quality)
                # Every worker in the paid group must be paid at least their minimum wage expectation.
                if (crossMultiplacationFormula >= worker.wage):
                    wages.append(crossMultiplacationFormula)
        return wages
    
    def findMinWorkers(self, k, wages, index, answer, minWage):
        if (len(answer) == k):
            minWage[0] = min(minWage[0], sum(answer))
            print answer
            return
        for i in range(index, len(wages)):
            self.findMinWorkers(k, wages, i+1, answer+[wages[i]], minWage)
        
    def mincostToHireWorkers(self, quality, wage, K):
        # create worker objects
        workers = self.createWorkers(quality, wage)
        mainMinWage = float('inf')
        # select main worker and determine other worker's wages
        for worker in workers:
            wages = self.wageDetermination(worker, workers)
            minWage = [float('inf')]
            print "For main worker with wage", worker.wage,"Quality",worker.quality
            self.findMinWorkers(K-1, wages, 0, [], minWage)
            mainMinWage = min(mainMinWage, worker.wage+minWage[0])
            print mainMinWage
        return mainMinWage
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        
