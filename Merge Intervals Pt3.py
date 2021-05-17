# Merge Intervals
# https://leetcode.com/problems/merge-intervals/
class Solution(object):
    def mergeIntervals(self, intervals, index):
        #print intervals, index
        if(index == len(intervals)-1):
            return
        # if intervals overlap then merge them
        currI = intervals[index]
        nextI = intervals[index+1]
        if(nextI[0] <= currI[1]):
            newI = [currI[0], max(nextI[1], currI[1])]
            intervals.pop(index)
            intervals.pop(index)
            intervals.insert(index, newI)
        else:
            index = index + 1
        self.mergeIntervals(intervals, index)
        
    def sortAccordingToStartTime(self, intervals):
        intervals.sort(key=lambda x:x[0])
        
    def merge(self, intervals):
        if not intervals:
            return []
        self.sortAccordingToStartTime(intervals)
        self.mergeIntervals(intervals, 0)
        return intervals
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
