#Max points on a line
# https://leetcode.com/problems/max-points-on-a-line/description/
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
class pointList(object):
    def __init__(self, pList):
        self.pList = []
        for p in pList:
            point = Point(p[0], p[1])
            self.pList.append(point)
    def getList(self):
        return self.pList
        
class firstApproach(object):
    def __init__(self, inputList):
        self.inputList = inputList

    #Function to check if 3 points are in same line or not.
    #The logic of this function is, if area of a triangle on plane is 0 then 3 points are in same line
    def inLine(self, p1, p2, p3):
        if ((p1[0]*p2[1]) + (p2[0]*p3[1]) + (p3[0]*p1[1]) - (p1[0]*p3[1]) - (p2[0]*p1[1]) - (p3[0]*p2[1]) == 0):
            return True
        return False

    def logic(self):
        if(len(self.inputList)==1):
            return 1
        if(len(self.inputList)==2):
            return 2
        path = []
        pathCount = 0
        mainCount = 0
        for i in range(0, len(self.inputList)-2):
            #print "i "+str(i)
            #do not add duplicates
            if not [self.inputList[i].x, self.inputList[i].y] in path:
                path.append([self.inputList[i].x, self.inputList[i].y])
            pathCount = pathCount+1
            for j in range(i+1, len(self.inputList)-1):
                #print "j "+str(j)
                if not [self.inputList[j].x, self.inputList[j].y] in path:
                    path.append([self.inputList[j].x, self.inputList[j].y])
                pathCount = pathCount+1
                for k in range(j+1, len(self.inputList)):
                    #print "k "+str(k)
                    if(len(path) == 1 or self.inLine(path[-1], path[-2], [self.inputList[k].x, self.inputList[k].y])):
                        if not [self.inputList[k].x, self.inputList[k].y] in path:
                            path.append([self.inputList[k].x, self.inputList[k].y])
                        pathCount = pathCount+1
                        #print path
                if pathCount > mainCount:
                    mainCount = pathCount
                    print path
                path = []
                pathCount = 0
                path.append([self.inputList[i].x, self.inputList[i].y])
                pathCount = pathCount+1
            path = []
            pathCount = 0
            print "---"
        print mainCount
        



#Main Program
#pl = pointList([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
#pl = pointList([[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],[-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],[60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]])
pl = pointList([[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],[5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],[0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],[-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],[-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],[-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],[-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86],[2,77],[-2,-49],[1,76],[-3,-38],[-8,7],[-17,-37],[5,72],[10,-37],[-4,-57],[-3,-53],[3,74],[-3,-11],[-8,7],[1,88],[-12,42],[1,-37],[2,77],[-6,77],[5,72],[-4,-57],[-18,-33],[-12,42],[-9,86],[2,77],[-8,77],[-3,77],[9,-42],[16,41],[-29,-37],[0,-41],[-21,18],[-27,-34],[0,77],[3,74],[-7,-69],[-21,18],[27,146],[-20,13],[21,130],[-6,-65],[14,-4],[0,3],[9,-5],[6,-29],[-2,73],[-1,-15],[1,76],[-4,77],[6,-29]])
l = pl.getList()
fa = firstApproach(l)
fa.logic()
