#Employee Free Time
#https://leetcode.com/problems/employee-free-time/
class Solution1(object):
    def __init__(self):
        self.intervals = None
    
    def findHighestAndLowestInterval(self, schedule):
        highInterval = 0
        lowestInterval = 10**8
        for employee in schedule:
            for interval in employee:
                if(interval[0] < lowestInterval):
                    lowestInterval = interval[0]
                if(interval[1] > highInterval):
                    highInterval = interval[1]
        return lowestInterval, highInterval

    def markIntervals(self, schedule):
        for employeeInterval in schedule:
            for interval in employeeInterval:
                for intervalTime in range(interval[0], interval[1]):
                    self.intervals[intervalTime] = 1

    def collectFreeTime(self, lowestInterval):
        i = lowestInterval
        output = []
        while(i < len(self.intervals)):
            j = i
            while(self.intervals[j] == 0):
                j = j + 1
            if(i != j):
                output.append([i, j])
                i = j + 1
            else:
                i = i+1
        return output
            
    def employeeFreeTime(self, schedule):
        lowestInterval, highInterval = self.findHighestAndLowestInterval(schedule)
        self.intervals = [0 for i in range(highInterval)]
        self.markIntervals(schedule)
        return self.collectFreeTime(lowestInterval)
        """
        :type schedule: List[List[List[int]]]
        :rtype: List[List[int]]
        """

class Solution2(object):
    def flattenAndSortIntervals(self,schedule):
        output = []
        for employeeTime in schedule:
            for interval in schedule:
                for time in interval:
                    output.append(time)
        output.sort()
        return output

    def combineIntervals(self, intervals):
        output = []
        while(intervals):
            i = 1
            while(i < len(intervals) and intervals[0][0] <= intervals[i][0] and intervals[0][1] >= intervals[i][0]):
                if(intervals[0][1] < intervals[i][1]):
                    intervals[0][1] = intervals[i][1]
                i = i + 1
            output.append(intervals[0])
            #pop the intervals
            j = 0
            while(intervals and j<i):
                intervals.pop(0)
                j = j+1
        return output

    def findGap(self, intervals):
        output = []
        for i in range(1, len(intervals)):
            if(intervals[i-1][1] < intervals[i][0]):
                output.append([intervals[i-1][1], intervals[i][0]])
        return output

    def employeeFreeTime(self, schedule):
        intervals = self.flattenAndSortIntervals(schedule)
        combinedIntervals = self.combineIntervals(intervals)
        return self.findGap(combinedIntervals)
        """
        :type schedule: List[List[List[int]]]
        :rtype: List[List[int]]
        """
#Main
obj1 = Solution1()
print obj1.employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]])
obj1 = Solution2()
print obj1.employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]])

obj2 = Solution1()
print obj2.employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]])
obj2 = Solution2()
print obj2.employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]])

obj3 = Solution1()
print obj3.employeeFreeTime([[[45,56],[89,96]],[[5,21],[57,74]]])
obj3 = Solution2()
print obj3.employeeFreeTime([[[45,56],[89,96]],[[5,21],[57,74]]])
