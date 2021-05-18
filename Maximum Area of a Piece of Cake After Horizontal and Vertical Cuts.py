# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
class Solution(object):
    
    # returns the tallest piece of cake after cuttin it vertically
    def verticallyCutCake(self, w, verticalCuts):
        widthPieces = []
        previous = 0
        for cut in verticalCuts:
            widthPieces.append(abs(previous - cut))
            previous = cut
        # final cut
        widthPieces.append(abs(previous - w))
        print widthPieces
        return max(widthPieces)
    
    # returns widest piece of cake after cutting it horizontally
    def horizontallyCutCake(self, h, horizontalCuts):
        heightPieces = []
        previous = 0
        for cut in horizontalCuts:
            heightPieces.append(abs(previous - cut))
            previous = cut
        # final cut
        heightPieces.append(abs(previous - h))
        print heightPieces
        return max(heightPieces)
        
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        height = self.horizontallyCutCake(h, sorted(horizontalCuts))
        width = self.verticallyCutCake(w, sorted(verticalCuts))
        return (width * height) % (10**9 + 7)
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        
