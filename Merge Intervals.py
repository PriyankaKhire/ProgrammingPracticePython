#Merge Intervals
#https://leetcode.com/problems/merge-intervals/description/
class Approch1(object):
    def __init__(self,intervals):
        self.intervals = intervals
        self.intervals.sort()

    def solution(self):
        output = []
        i = 0
        while (i < len(self.intervals)):
            currInterval = self.intervals[i]
            while( i+1 < len(self.intervals) and (self.intervals[i+1][0] >= currInterval[0] and self.intervals[i+1][0] <= currInterval[1])):
                currInterval[1] = max(self.intervals[i+1][1], currInterval[1])
                i = i+1
            i = i+1
            output.append(currInterval)
        print output

#Main Program
o = Approch1([[1,3],[8,10],[15,18], [2,6]])
o.solution()

o = Approch1([[1,9],[2,5],[19,20],[10,11],[12,20],[0,3],[0,1],[0,2]])
o.solution()
            
            
