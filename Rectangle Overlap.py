#Rectangle Overlap
# https://leetcode.com/problems/rectangle-overlap/solution/
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        x1 = [rec1[0], rec1[2]]
        x2 = [rec2[0], rec2[2]]
        y1 = [rec1[1], rec1[3]]
        y2 = [rec2[1], rec2[3]]
        # if both are equal
        if(rec1 == rec2):
            return True
        # if x2 inside x1
        if(x1[0] <= x2[0] and x1[1] > x2[0] and x1[1] > x2[0]):
            if(y1[0] <= y2[0] and y1[1] > y2[0] and y1[1] > y2[0]):
                return True
            elif(y2[0] <= y1[0] and y2[1] > y2[0] and y2[1] > y1[0]):
                return True
        # if x1 inside x2
        if(x2[0] <= x1[0] and x2[1] > x1[0] and x2[1] > x1[0]):
            if(y2[0] <= y1[0] and y2[1] > y2[0] and y2[1] > y1[0]):
                return True
            elif(y1[0] <= y2[0] and y1[1] > y2[0] and y1[1] > y2[0]):
                return True
        return False
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
