# Rectangle Overlap
# https://leetcode.com/problems/rectangle-overlap/
class Rectangle(object):
    def __init__(self, rec):
        # bottom left
        self.x1 = rec[0]
        self.y1 = rec[1]
        # top right
        self.x2 = rec[2]
        self.y2 = rec[3]
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        r1 = Rectangle(rec1)
        r2 = Rectangle(rec2)
        # in order to better understand please draw these 4 conditions and see.
        # there are 4 conditions when a rectangle doesn't overlap another
        # 1) if a rectangle is totally to the right of another rectangle
        # (r1.x1 > r2.x2)
        # x1y2----x2y2  x1y2----x2y2
        #       | r2 |            | r1 |
        # x1y1----x2y1  x1y1----x2y1
        #2) if a rectangle is totally to the left of another rectangle
        # (r1.x2 < r2.x1)
        # x1y2----x2y2  x1y2----x2y2
        #       | r1 |            | r2 |
        # x1y1----x2y1  x1y1----x2y1
        #3) if a rectangle is totally below another rectangle
        # (r1.y2 < r2.y1)
        # x1y2----x2y2
        #      | r2 |
        # x1y1----x2y1
        # x1y2----x2y2
        #      | r1 |
        # x1y1----x2y1
        #4) if a rectangle is totally above another rectangle
        # (r1.y1 > r2.y2)
        # x1y2----x2y2
        #      | r1 |
        # x1y1----x2y1
        # x1y2----x2y2
        #      | r2 |
        # x1y1----x2y1
        # so the condition for NON overlap is cond1 or cond2 or cond3 or cond4
        if((r1.x1 >= r2.x2) or (r1.x2 <= r2.x1) or (r1.y2 <= r2.y1) or (r1.y1 >= r2.y2)):
            return False
        return True
        

# Main
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
obj = Solution()
print obj.isRectangleOverlap(rec1, rec2)

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
obj = Solution()
print obj.isRectangleOverlap(rec1, rec2)
