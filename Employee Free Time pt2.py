# Employee Free Time
# https://leetcode.com/problems/employee-free-time/submissions/
"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution(object):
    def employeeFreeTime(self, schedule):
        # flatten the list
        avails = []
        for employee in schedule:
            avails.extend(employee)
        # sort them by start time
        avails = sorted(avails, key=lambda x: x.start)
        # merge them
        s = avails[0].start
        e = avails[0].end
        merge = []
        for i in range(1, len(avails)):
            # if interval can be merged
            if(avails[i].start >= s and avails[i].start <= e):
                # to merge interval 2,3 in 1,4 we have following condition
                if(avails[i].end >= e):
                    e = avails[i].end
            else:
                merge.append([s,e])
                s = avails[i].start
                e = avails[i].end
        # append final interval
        merge.append([s,e])
        # find final free time
        freeTime = []
        for i in range(1, len(merge)):
            interval = Interval()
            interval.start = merge[i-1][1]
            interval.end = merge[i][0]
            freeTime.append(interval)
        return freeTime
        """
        :type schedule: list<list<Interval>>
        :rtype: list<Interval>
        """
        
