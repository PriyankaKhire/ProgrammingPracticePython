# Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/
class Meeting(object):
    def __init__(self, s, e):
        self.start = s
        self.end = e
        
class Solution(object):
    def canAttendMeetings(self, intervals):
        # sort intervals according to start time
        meetingIntervals = [Meeting(i[0], i[1]) for i in intervals]
        meetingIntervals.sort(key=lambda x: x.start)
        # just check if the next meeting start or end time falls between previsou meeting's start or end times.
        for i in range(len(meetingIntervals)-1):
            if(meetingIntervals[i+1].start >= meetingIntervals[i].start and meetingIntervals[i+1].start < meetingIntervals[i].end):
                return False
        return True
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
