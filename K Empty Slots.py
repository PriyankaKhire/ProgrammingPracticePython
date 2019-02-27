#K Empty Slots
#https://leetcode.com/problems/k-empty-slots/
class Bruteforce(object):
    def __init__(self):
        self.flowerBed = []

    def checkKFlowersBetween2BloomingFlowers(self, k):
        print self.flowerBed
        i = 0
        while(i < len(self.flowerBed)):
            if(self.flowerBed[i] == False):
                i = i+1
                continue
            j = 0
            while(i+j+1 < len(self.flowerBed) and self.flowerBed[i+j+1] == False):
                j = j+1
            if(i+j+1 < len(self.flowerBed) and self.flowerBed[i+j+1] == True and j ==k):
                return True
            i = j+i+1
        return False

    def fillFlowerBed(self, flowers, k):
        for i in range(len(flowers)):
            self.flowerBed[flowers[i]-1] = True
            if(self.checkKFlowersBetween2BloomingFlowers(k)):
                return i+1
        return -1
        
    def kEmptySlots(self, flowers, k):
        self.flowerBed = [False for i in range(len(flowers))]
        print self.fillFlowerBed(flowers, k)
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
class LookAroundApproch(object):
    def __init__(self):
        self.flowerBed = []

    def isValid(self, window):
        if(window < len(self.flowerBed) and window >= 0):
            return True
        return False

    def lookInWindow(self, low, high, k):
        if(self.flowerBed[low] == True and  self.flowerBed[high] == True):
            for i in range(low+1, high):
                if not(self.flowerBed[i] == False):
                    return False
            return True
        return False

    #create a window around i that satisfies the k condition
    def lookAround(self, slot, k):
        print self.flowerBed
        #create a window on left
        print "left window ", slot-k-1
        if(self.isValid(slot-k-1) and self.lookInWindow(slot-k-1, slot, k)):
            return True
        print "right window ", slot+k+1
        if(self.isValid(slot+k+1) and self.lookInWindow(slot, slot+k+1, k)):
            return True
        return False
            

    def fillFlowerBed(self, flowers, k):
        for i in range(len(flowers)):
            self.flowerBed[flowers[i]-1] = True
            print "slot = ", flowers[i]-1
            if(self.lookAround(flowers[i]-1, k)):
                return i+1
        return -1
        
    def kEmptySlots(self, flowers, k):
        self.flowerBed = [False for i in range(len(flowers))]
        print self.fillFlowerBed(flowers, k)
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """

#Main
obj1 = Bruteforce()
obj1.kEmptySlots([1,3,2], 1)

obj2 = Bruteforce()
obj2.kEmptySlots([1,2,3], 1)

obj3 = LookAroundApproch()
obj3.kEmptySlots([1,3,2], 1)

obj4 = LookAroundApproch()
obj4.kEmptySlots([1,2,3], 1)
