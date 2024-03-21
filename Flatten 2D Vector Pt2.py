# Flatten 2D Vector
# https://leetcode.com/problems/flatten-2d-vector/
class Vector2D(object):

    def __init__(self, vec):
        self.vec = vec
        self.subList = 0
        self.listPtr = 0
        """
        :type vec: List[List[int]]
        """
        

    def next(self):
        print "sub list", self.subList, "list ptr", self.listPtr
        # 1. if current list is empty
        while(not self.vec[self.subList]):
            self.subList += 1
            self.listPtr = 0
        element = self.vec[self.subList][self.listPtr]
        self.listPtr += 1
        # 2. if current list does not have elements
        if (len(self.vec[self.subList]) == self.listPtr):
            self.subList += 1
            self.listPtr = 0
        return element
        """
        :rtype: int
        """
    
    def findNextListWithElements(self, subList):
        print "sublist", subList, not(self.vec[subList])
        while((len(self.vec) < subList) and not(self.vec[subList])):
            subList += 1
        print "sublist now", subList, len(self.vec)
        if (len(self.vec) == subList):
            return False
        if (self.vec[subList]):
            return True
        return False
        

    def hasNext(self):
        listPtr = self.listPtr
        subList = self.subList
        print "hasNext: subList", subList, "list Ptr", listPtr
        # if we are at end of vector
        if (len(self.vec) == subList):
            return False
        # if we are at the end of current list
        print len(self.vec[subList])
        if(len(self.vec[subList]) == listPtr):
            # find next list that has elements
            return self.findNextListWithElements(subList+1)
        # if we are not at the end of current list
        return True
        """
        :rtype: bool
        """
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()