# Most Profit Assigning Work
# https://leetcode.com/problems/most-profit-assigning-work/description/
# how to sort a list of tuples https://learnpython.com/blog/sort-tuples-in-python/
# Sorting a List by the Second Element of the Tuple: tupList.sort(key=lambda a: a[1])
class Solution(object):
    def __init__(self):
        # will contain tupul (difficulty, profit)
        self.difficultyAndProfit = []
    
    # This function fills the self.difficultyAndProfit with jobs that don't have difficulty more than our workers can handle
    def createTup(self, difficulty, profit, worker):
        maxDifficulty = max(worker)
        for i in range(len(difficulty)):
            if (difficulty[i] > maxDifficulty):
                continue
            self.difficultyAndProfit.append((difficulty[i], profit[i]))

    def maxProfitAssignment(self, difficulty, profit, worker):
        self.createTup(difficulty, profit, worker)
        # None of the workers can do any job
        if not self.difficultyAndProfit:
            return 0
        # sort the workers
        worker = sorted(worker)
        # sort the list of tuples by difficulty
        self.difficultyAndProfit.sort()
        # 2 pointer approach
        workerIndex = 0
        tupIndex = 0
        prevWorkerProfit = 0
        maxProfit = 0
        while(workerIndex < len(worker)):
            workerProfit = 0
            while(tupIndex < len(self.difficultyAndProfit) and self.difficultyAndProfit[tupIndex][0] <= worker[workerIndex]):
                workerProfit = max(workerProfit, self.difficultyAndProfit[tupIndex][1])
                tupIndex += 1
            # compare profit with previous worker, if they have a more profitable job then do that job instead
            workerProfit = max(workerProfit, prevWorkerProfit)
            maxProfit += workerProfit
            prevWorkerProfit = workerProfit
            workerIndex += 1
        return maxProfit
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        
