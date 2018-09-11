#Meeting Rooms II
#https://leetcode.com/problems/meeting-rooms-ii/description/
class Interval(object):
     def __init__(self, s, e):
         self.start = s
         self.end = e
         
class Solution(object):
    def __init__(self):
        self.meetingRoom = 1
        self.allocation = {}

    #find ALL interval that begins after or at the end time
    def binarySearch(self, intervals, endTime):
        low = 0
        high = len(intervals)-1
        while(low <= high):
            mid = (low+high)/2
            interval = intervals[mid]
            if(interval.start == endTime):
                low = mid
                break
            if(interval.start < endTime):
                low = mid+1
            else:
                high = mid-1
        if (low <= (len(intervals)-1)):
            output = []
            for i in range(low, len(intervals)):
                output.append(intervals[i])
            return output
        return False
        
    def minMeetingRooms(self, intervals):
        #sort intervals according to their start intervals
        intervals.sort(key=lambda x: x.start, reverse=False)
        print "After sorting"
        for interval in  intervals:
            print "[",interval.start, ",",interval.end,"]"
        print ""
        for interval in intervals:
            endTime = interval.end
            if not(interval in self.allocation):
                self.allocation[interval] = self.meetingRoom
                self.meetingRoom = self.meetingRoom+1
            #find first interval that is not assigned a room
            #essentially the goal is to find an interval that requires a room all to itself.
            anotherIntervals = self.binarySearch(intervals, endTime)
            if(anotherIntervals):
                for ai in anotherIntervals:
                    if not(ai in self.allocation):
                        self.allocation[ai] = self.allocation[interval]
                        break                    
        for interval in  self.allocation:
            print interval.start, interval.end," = ",self.allocation[interval]
        print ""
        print "Total meeting rooms required ",self.meetingRoom-1
        print ""

#Main
o1 = Solution()
o1.minMeetingRooms([Interval(1, 10), Interval(2, 7), Interval(3, 19), Interval(8, 12), Interval(11, 12),Interval(11, 13),Interval(11, 20), Interval(11, 30)])
o2 = Solution()
o2.minMeetingRooms([Interval(5,10),Interval(0,30),Interval(15,20)])
o3 = Solution()
o3.minMeetingRooms([Interval(1293,2986),Interval(848,3846),Interval(4284,5907),Interval(4466,4781),Interval(518,2918),Interval(300,5870)])
