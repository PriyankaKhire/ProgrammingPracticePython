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
        if ((p1.x*p2.y) + (p2.x*p3.y) + (p3.x*p1.y) - (p1.x*p3.y) - (p2.x*p1.y) - (p3.x*p2.y) == 0):
            return True
        return False

    def logic(self):
        if(len(self.inputList)==1):
            return 1
        if(len(self.inputList)==2):
            return 2
        path = []
        mainPath = []
        for i in range(0, len(self.inputList)-2):
            print "i "+str(i)
            path.append([self.inputList[i].x, self.inputList[i].y])
            for j in range(i+1, len(self.inputList)-1):
                print "j "+str(j)
                path.append([self.inputList[j].x, self.inputList[j].y])
                for k in range(j+1, len(self.inputList)):
                    print "k "+str(k)
                    if(self.inLine(self.inputList[i], self.inputList[j], self.inputList[k])):
                        path.append([self.inputList[k].x, self.inputList[k].y])
                        print path
                if len(path) > len(mainPath):
                    mainPath = path
                path = []
                path.append([self.inputList[i].x, self.inputList[i].y])
            path = []
            print "---"
        print mainPath
        



#Main Program
#pl = pointList([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
pl = pointList([[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],[-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],[60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]])
l = pl.getList()
fa = firstApproach(l)
fa.logic()
