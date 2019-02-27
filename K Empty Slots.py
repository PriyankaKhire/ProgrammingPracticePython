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

#Main
obj1 = Bruteforce()
obj1.kEmptySlots([1,3,2], 1)

obj2 = Bruteforce()
obj2.kEmptySlots([1,2,3], 1)
