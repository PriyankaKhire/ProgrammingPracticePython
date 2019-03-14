#Segment Tree for 1D array
class SegmentTree(object):
    def __init__(self, array):
        self.array = array
        self.tree = []

    def findNearestGreaterPower2(self, num):
        n = 1
        while(2**n < num):
            n = n+1
        return 2**n

    def segmentTreeOperation(self, parentIndex, leftChildIndex, rightChildIndex):
        print "Filling the parent index ", parentIndex, " with minimum of ", self.tree[leftChildIndex], " and ", self.tree[rightChildIndex]
        #lets say this is a min segment tree
        #meaning at given range we wanna find the min number.
        self.tree[parentIndex] = min(self.tree[leftChildIndex], self.tree[rightChildIndex])
            
    def getTreeArraySize(self):
        #if the length of input array is power of 2 example 4 or 8 then the tree can be a complete binary tree
        #in that case the size of array required to hold the tree is 2*len(array) -1
        #find the nearest power of 2 that is greater than the length
        #so if the length is 5 then nearest power of 2 that is greater than 5 is 8
        treeSize = (2*(self.findNearestGreaterPower2(len(self.array)))) - 1
        self.tree = [None for i in range(treeSize)]

    def fillTree(self, level, low, high, parentIndex):
        print "currently at level ", level, " in the tree"
        if(low == high):
            #filling leaves of the tree
            print "put number ", self.array[low], " in index ", parentIndex, " in the tree"
            self.tree[parentIndex] = self.array[low]
            #I know I am not using the level parameter, its just for your understanding at what level are we in tree
            return
        mid = (low+high)/2
        #go left
        #for a parent the left child is located at index 2*parentIndex +1
        self.fillTree(level+1, low, mid, (2*parentIndex)+1)
        #go right
        #for a parent the right child is located at index 2*parentIndex +2
        self.fillTree(level+1, mid+1, high, (2*parentIndex)+2)
        #once we have filled the left child and right child, we now proceed to fill the parent based on given condition
        self.segmentTreeOperation(parentIndex, (2*parentIndex)+1, (2*parentIndex)+2)

    def partialOverlap(self, currentRange, queryRange, parentIndex):
        #three stages of overlap
        #1) query range falls under current range
        #cr -------------------------
        #qr          ----------
        if(currentRange[0] <= queryRange[0] and currentRange[1] >= queryRange[1]):
            #go both direcitons
            return True, "both"
        #2)second part of current range falls under query range
        #cr -------
        #qr       ---------
        if(currentRange[0] <= queryRange[0] and currentRange[1] >= queryRange[0] and currentRange[1] <= queryRange[1]):
            #go right
            return True, "right"
        #3)first part of current range falls under query range
        #cr         -------------
        #qr -----------
        if(currentRange[0] >= queryRange[0] and currentRange[0] <= queryRange[1] and currentRange[1] >= queryRange[1]):
            return True, "left"
        return False, "none"
             
        
    def find(self, currentRange, queryRange, parentIndex):
        print currentRange, queryRange, parentIndex
        #find if partial overlap
        flag, direction  = self.partialOverlap(currentRange, queryRange, parentIndex)
        if(flag):
            mid = (currentRange[0] + currentRange[1])/2
            if(direction == "both"):
                self.find([currentRange[0], mid], queryRange, (2*parentIndex)+1)
                self.find([mid+1, currentRange[1]], queryRange, (2*parentIndex)+2)
            elif(direction == "right"):
                self.find([mid+1, currentRange[1]], queryRange, (2*parentIndex)+2)
            else:
                self.find([currentRange[0], mid], queryRange, (2*parentIndex)+1)
        

    def logic(self):
        self.getTreeArraySize()
        self.fillTree(0, 0, len(self.array)-1, 0)
        print self.tree
        print self.find([0, len(self.array)-1], [2,4], 0)

#Main
obj = SegmentTree([1,2,3,4,5,6])
obj.logic()
