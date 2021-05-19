# Maximum Profit in Job Scheduling
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
class Solution(object):
    
    def logic(self, tupleList, index, profit, previousJobEndTime, maxProfit):
        #print tupleList, index, profit, previousJobEndTime
        if(index <= len(tupleList)):
            maxProfit[0] = max(maxProfit[0], profit)
        for i in range(index, len(tupleList)):
            if(previousJobEndTime == 0 or tupleList[i][0] >= previousJobEndTime):
                self.logic(tupleList, i+1, profit+tupleList[i][2], tupleList[i][1], maxProfit)

    def jobScheduling(self, startTime, endTime, profit):
        tupleList = sorted(list(set(zip(startTime, endTime, profit))), key=lambda x:x[0])
        maxProfit = [0]
        self.logic(tupleList, 0, 0, 0, maxProfit)
        return maxProfit[0]
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        
