#Max points on a line
# https://leetcode.com/problems/max-points-on-a-line/description/
class point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
        
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
'''
p1 = point(1,1)
p2 = point(2,2)
p3 = point(3,3)
fa = firstApproach([p1,p2,p3])
'''
p1 = point(1,1)
p2 = point(3,2)
p3 = point(5,3)
p4 = point(4,1)
p5 = point(2,3)
p6 = point(1,4)
fa = firstApproach([p1,p2,p3,p4,p5,p6])
fa.logic()
