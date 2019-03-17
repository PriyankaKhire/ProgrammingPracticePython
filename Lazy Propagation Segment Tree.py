#Lazy Propagation Segment Tree
#building min lazy propogation segment tree
class LazySegmentTree(object):
    def __init__(self, array):
        self.array = array
        self.tree = []
        #to keep track of increment and decrement only
        self.lazyTree = []

    def findNearestPowerOf2(self, num):
        powerOf2 = 0
        while(2**powerOf2 < num):
            powerOf2 = powerOf2+1
        return powerOf2
    
    def treeSize(self):
        nearestPowerOf2 = self.findNearestPowerOf2(len(self.array))
        sizeOfTree = (2*(2**nearestPowerOf2)) -1
        return sizeOfTree

    def treeOperation(self, left, right):
        return min(left, right)

    def buildTree(self, low, high, treeParentIndex):
        if(high == low):
            self.tree[treeParentIndex] = self.array[low]
            return
        mid = (high+low)/2
        #go left
        self.buildTree(low, mid, (2*treeParentIndex)+1)
        #go right
        self.buildTree(mid+1, high, (2*treeParentIndex)+2)
        #tree Operation
        self.tree[treeParentIndex] = self.treeOperation(self.tree[(2*treeParentIndex)+1], self.tree[(2*treeParentIndex)+2])

    def isPartialOverlap(self, queryRange, currentRange):
        #cr --------------------
        #qr       ---------
        if(currentRange[0] <= queryRange[0] and currentRange[1] >= queryRange[1]):
            return True, 'both'
        #cr -----------
        #qr          -----------
        if(currentRange[0] <= queryRange[0] and currentRange[1] >= queryRange[0] and currentRange[1] < queryRange[1]):
            return True, 'right'
        #cr       ----------
        #qr ----------
        if(currentRange[0] >= queryRange[0] and currentRange[0] <= queryRange[1] and currentRange[1] >= queryRange[1]):
            return True, 'left'
        return False, 'none'

    def ifCompleteOverlap(self, queryRange, currentRange):
        if(queryRange == currentRange):
            return True
        #cr     -----
        #qr ------------
        if(currentRange[0] >= queryRange[0] and currentRange[1] <= queryRange[1]):
            return True
    
    def overlap(self, queryRange, currentRange):
        #complete overlap
        if(self.ifCompleteOverlap(queryRange, currentRange)):
            return "Complete overlap", -1
        #partial overlap
        flag, direction = self.isPartialOverlap(queryRange, currentRange)
        if(flag):
            return "Partial overlap", direction
        #no overlap
        return "No overlap", -1

    def applyPastUpdatesFromLazyTree(self,parentIndex):
        #apply any last updates that have not been applied
        self.tree[parentIndex] = self.tree[parentIndex]+self.lazyTree[parentIndex]
        #propogate the update to its childern
        if((2*parentIndex)+2 < len(self.tree)):
            self.lazyTree[(2*parentIndex)+1] = self.lazyTree[(2*parentIndex)+1] + self.lazyTree[parentIndex]
            self.lazyTree[(2*parentIndex)+2] = self.lazyTree[(2*parentIndex)+2] + self.lazyTree[parentIndex]
        #since we have now applied the update we can update values in lazy tree
        self.lazyTree[parentIndex] = 0
                

    def find(self, queryRange, currentRange, parentIndex):
        self.applyPastUpdatesFromLazyTree(parentIndex)
        #find what type of overlap
        overlap, direction = self.overlap(queryRange, currentRange)
        if(overlap == 'Complete overlap'):
            return self.tree[parentIndex]
        if(overlap == 'Partial overlap'):
            mid = (currentRange[0]+currentRange[1])/2
            #if(direction == 'both'):
            #because this is lazy propogation tree I want it to go to both directions
            #even if it doesnt overlap the other sub tree we want the childern to be updated together.
            return self.treeOperation(self.find(queryRange, [currentRange[0], mid], (parentIndex*2)+1), self.find(queryRange, [mid+1, currentRange[1]], (2*parentIndex)+2))
            #if(direction == 'left'):
                #return self.find(queryRange, [currentRange[0], mid], (parentIndex*2)+1)
            #if(direction == 'right'):
                #return self.find(queryRange, [mid+1, currentRange[1]], (parentIndex*2)+2)
        if(overlap == 'No overlap'):
            return 99999999

    def increment(self, incrementNumber, queryRange, currentRange, parentIndex):
        self.applyPastUpdatesFromLazyTree(parentIndex)
        overlap, direction = self.overlap(queryRange, currentRange)
        if(overlap == 'Complete overlap'):
            #update the tree
            self.tree[parentIndex] = self.tree[parentIndex]+incrementNumber
            #update lazy tree childern
            if((2*parentIndex)+2 < len(self.tree)):
                self.lazyTree[(2*parentIndex)+1] = self.lazyTree[(2*parentIndex)+1] + incrementNumber
                self.lazyTree[(2*parentIndex)+2] = self.lazyTree[(2*parentIndex)+2] + incrementNumber
            return
        if(overlap == 'Partial overlap'):
            mid = (currentRange[0]+currentRange[1])/2
            if(direction == 'both'):
                self.increment(incrementNumber, queryRange, [currentRange[0], mid], (parentIndex*2)+1)
                self.increment(incrementNumber, queryRange, [mid+1, currentRange[1]], (2*parentIndex)+2)
            if(direction == 'left'):
                self.increment(incrementNumber, queryRange, [currentRange[0], mid], (parentIndex*2)+1)
            if(direction == 'right'):
                self.increment(incrementNumber, queryRange, [mid+1, currentRange[1]], (parentIndex*2)+2)
        if(overlap == 'No overlap'):
            return
        #update the new current value
        self.tree[parentIndex] = self.treeOperation(self.tree[(2*parentIndex)+1], self.tree[(2*parentIndex)+2])
                
            
        
    def logic(self):
        #tree size
        self.tree = [0 for i in range(self.treeSize())]
        self.lazyTree = [0 for i in range(self.treeSize())]
        #build the tree
        self.buildTree(0, len(self.array)-1, 0)
        #operations
        print self.find([1,2], [0, len(self.array)-1], 0)
        self.increment(3, [0,3], [0, len(self.array)-1], 0)
        print self.tree, self.lazyTree
        self.increment(1, [0,3], [0, len(self.array)-1], 0)
        print self.tree, self.lazyTree
        self.increment(2, [0,0], [0, len(self.array)-1], 0)
        print self.tree, self.lazyTree
        print self.find([3,5], [0, len(self.array)-1], 0)
        print self.tree, self.lazyTree


#Main
obj = LazySegmentTree([-1,2,4,1,7,1,3,2])
obj.logic()
