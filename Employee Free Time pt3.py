# Employee Free Time
# https://leetcode.com/problems/employee-free-time/
"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def flattenList(self, schedule):
        intervals = []
        for listInterval in schedule:
            for interval in listInterval:
                intervals.append(interval)
        return intervals
    
    def isOverlap(self, i1, i2):
        if (i1.start <= i2.start):
            if (i1.end >= i2.start):
                return True
        return False
    
    def merge(self, i1, i2):
        i1.end = max(i1.end, i2.end)
    
    def printIntervals(self, intervals):
        for i in intervals:
            print i.start, i.end
        print "*"*20
    
    def mergeIntervals(self, intervals):
        # sort based on start times
        intervals.sort(key=lambda x: x.start)
        index = 0
        while (index < len(intervals)-1):
            #self.printIntervals(intervals)
            if (self.isOverlap(intervals[index], intervals[index+1])):
                self.merge(intervals[index], intervals[index+1])
                # pop out index+ interval coz we have made changes to it
                intervals.pop(index+1)
            else:
                index = index+1
        return intervals
    
    def findFreeTime(self, intervals):
        freeIntervals = []
        for i in range(len(intervals)-1):
            interval = Interval(intervals[i].end, intervals[i+1].start)
            freeIntervals.append(interval)
        return freeIntervals
            
    def employeeFreeTime(self, schedule):
        intervals = self.flattenList(schedule)
        mergedIntervals = self.mergeIntervals(intervals)
        return self.findFreeTime(mergedIntervals)
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        
