#The Skyline Problem
#https://leetcode.com/problems/the-skyline-problem/description/

class Solution(object):
    def __init__(self):
        self.points = []

    def addPoints(self, point):
        if point in self.points:
            while (point in self.points):
                self.points.remove(point)
            return
        self.points.append(point)

    def discardPoints(self, nsp, nep, sp, ep):
        if(nsp[1] > sp[1]):
            print "discard point ", nsp
            nsp = None
        if(nep[1] > sp[1]):
            print "discard point ", nep
            nep = None
        return nsp, nep


    def raisePoints(self, currBuilding, buildings):
        sp, ep = self.generateStartAndEndPoints(currBuilding)
        for building in buildings:
            if(currBuilding == building):
                continue
            x1 = building[0]
            x2 = building[1]
            h = building[2]
            if((sp[0] >= x1 and sp[0] <= x2) and (sp[1] < h)):
                #print sp, " falls between building ", building
                sp[1] = h
            #make sure 2 end points are not same thats why check ep != x2, 0
            if((ep[0] >= x1 and ep[0] <= x2) and (ep[1] < h) and (ep != [x2, 0])):
                #print ep, " falls between building", building
                ep[1] = h
        return sp, ep
        
    
    def generateStartAndEndPoints(self, building):
        return [building[0], building[2]], [building[1], 0]
    
    def getSkyline(self, buildings):
        for building in buildings:
            sp, ep = self.generateStartAndEndPoints(building)
            nsp, nep = self.raisePoints(building, buildings)
            nsp, nep = self.discardPoints(nsp, nep, sp, ep)
            if nsp:
                self.addPoints(nsp)
            if nep:
                self.addPoints(nep)
        print self.points   
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

#Main
o = Solution()
o.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8], [3,10,5] ])
print "==="
o1 = Solution()
o1.getSkyline([[0,1,3]])
print "==="
o2 = Solution()
o2.getSkyline([[0,2,3],[2,5,3]])
print "==="
o3 = Solution()
o3.getSkyline([[1,2,1],[1,2,2],[1,2,3]])

#does not work for [[0,3,3],[1,5,3],[2,4,3],[3,7,3]]
#this algo does not find points on same line
