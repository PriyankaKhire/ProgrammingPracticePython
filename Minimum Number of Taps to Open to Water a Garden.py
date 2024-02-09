# Minimum Number of Taps to Open to Water a Garden
# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/

class Solution(object):
    def createIntervals(self, ranges):
        intervals = []
        for i in range(len(ranges)):
            if (ranges[i] == 0):
                continue
            interval = [max(0, i - ranges[i]), i + ranges[i]]
            intervals.append(interval)
        # sort the intervals by start
        return sorted(intervals)
    
    def countIntervals(self, intervals, index, count, start, end, n, minCount):
        #print "Start", start, "end", end, "Count", count
        if (index == len(intervals) or end >= n):
            minCount[0] = min(count, minCount[0])
            return
        for i in range(index, len(intervals)):
            j = intervals[i]
            if (j[0] == 0 and j[1] == n):
                minCount[0] = 1
                return 
            if (start <= j[0] and j[0] <= end and end < j[1]):
                if (start == j[0]):
                    self.countIntervals(intervals, i+1, count, j[0], j[1], n, minCount)
                else:
                    self.countIntervals(intervals, i+1, count+1, j[0], j[1], n, minCount)

    def minTaps(self, n, ranges):
        intervals = self.createIntervals(ranges)
        if not intervals:
            return -1
        minCount = [n]
        self.countIntervals(intervals, 1, 1, intervals[0][0], intervals[0][1], n, minCount)
        return minCount[0]
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        
