#2D Segment Tree
from operator import add
class CommonFunctions(object):
    def treeSize(self, array):
        n = 0
        while(len(array) > (2**n)):
            n = n+1
        return 2*(2**n) - 1

    def partialOverlap(self, queryRange, currentRange):
        if(queryRange[0] > currentRange[0] and queryRange[1] < currentRange[1]):
            return True
        if(queryRange[0] <=  currentRange[0] and queryRange[1] >=  currentRange[0] and queryRange[1] <=  currentRange[1]):
            return True
        if(queryRange[0] >= currentRange[0] and queryRange[0] <= currentRange[1] and queryRange[1] >=  currentRange[1]):
            return True

    def completeOverlap(self, queryRange, currentRange):
        if(queryRange == currentRange):
            return True
        if(queryRange[0] <= currentRange[0] and queryRange[1] >= currentRange[1]):
            return True

    def typeOfOverlap(self, queryRange, currentRange):
        if(self.completeOverlap(queryRange, currentRange)):
            return "Complete"
        if(self.partialOverlap(queryRange, currentRange)):
            return "Partial"
        return None
    
class OneDSegmentTree(object):
    def __init__(self, array):
        self.array = array
        self.tree = []
        self.cf = CommonFunctions()

    def treeOperation(self, left, right, index):
        self.tree[index] = self.tree[left]+self.tree[right]

    def createTree(self, low, high, parentIndex):
        if(low == high):
            self.tree[parentIndex] = self.array[low]
            return
        mid = (low+high)/2
        #go left
        self.createTree(low, mid, (2*parentIndex)+1)
        #go right
        self.createTree(mid+1, high, (2*parentIndex)+2)
        #perform tree operation
        self.treeOperation((2*parentIndex)+1, (2*parentIndex)+2, parentIndex)

    def findQuery(self, queryRange, currentRange, treeIndex):
        overlap = self.cf.typeOfOverlap(queryRange, currentRange)
        if(overlap == "Complete"):
            return self.tree[treeIndex]
        if(overlap == "Partial"):
            mid = (currentRange[0]+currentRange[1])/2
            left = self.findQuery(queryRange, [currentRange[0], mid], (2*treeIndex)+1)
            right = self.findQuery(queryRange, [mid+1, currentRange[1]], (2*treeIndex)+2)
            return left+right
        if(overlap == None):
            return 0

    def find(self, queryRange):
        return self.findQuery(queryRange, [0, len(self.array)-1], 0)

    def logic(self):
        size = self.cf.treeSize(self.array)
        self.tree = [0 for i in range(size)]
        self.createTree(0, len(self.array)-1, 0)

class TwoDSegmentTree(object):
    def __init__(self, matrix):
        self.matrix = matrix
        #this array will hold rows of 1d segment tree
        self.array = [matrix[i] for i in range(len(matrix))]
        self.tree = []
        self.cf = CommonFunctions()

    def add2Lists(self, list1, list2):
        return list( map(add, list1, list2) )

    def treeOperation(self, left, right, index):
        obj = OneDSegmentTree([])
        obj.array = self.add2Lists(self.tree[left].array, self.tree[right].array)
        obj.tree = self.add2Lists(self.tree[left].tree, self.tree[right].tree)
        self.tree[index] = obj

    def createRowTree(self, row):
        obj = OneDSegmentTree(self.array[row])
        obj.logic()
        return obj

    def createTree(self, low, high, parentIndex):
        if(low == high):
            self.tree[parentIndex] = self.createRowTree(low)
            return
        mid = (low+high)/2
        #go left
        self.createTree(low, mid, (2*parentIndex)+1)
        #go right
        self.createTree(mid+1, high, (2*parentIndex)+2)
        #perform tree operation
        self.treeOperation((2*parentIndex)+1, (2*parentIndex)+2, parentIndex)

    def flattenList(self, array, output):
        for item in array:
            if isinstance(item, (list,)):
                self.flattenList(item, output)
            elif(item != None):
                output.append(item)
        return output

    def findRows(self, queryRange, currentRange, treeIndex):
        print queryRange, currentRange, treeIndex, 
        overlap = self.cf.typeOfOverlap(queryRange, currentRange)
        print overlap
        if(overlap == "Complete"):
            return self.tree[treeIndex]
        if(overlap == "Partial"):
            mid = (currentRange[0]+currentRange[1])/2
            left = self.findRows(queryRange, [currentRange[0], mid], (2*treeIndex)+1)
            right = self.findRows(queryRange, [mid+1, currentRange[1]], (2*treeIndex)+2)
            return [left, right]
        if(overlap == None):
            return None

    def find(self, queryRange):
        rowQueryRange = [queryRange[0][0], queryRange[1][0]]
        colQueryRange = [queryRange[0][1], queryRange[1][1]]
        queryRows = self.findRows(rowQueryRange, [0, len(self.matrix)-1], 0)
        #flatten the list
        rows = self.flattenList(queryRows, [])
        total = 0
        for row in rows:
            if(row):
                total = total + row.find(colQueryRange)
        return total
        

    def logic(self):
        size = self.cf.treeSize(self.array)
        self.tree = [None for i in range(size)]
        self.createTree(0, len(self.array)-1, 0)
        print self.tree
        for tree in self.tree:
            if(tree):
                print tree.tree

#Main
m1 = [
    [1,2,3,4],
    [5,6,7,8],
    [1,7,5,9],
    [3,0,6,2]
    ]
obj1 = TwoDSegmentTree(m1)
obj1.logic()
print obj1.find([[1,1], [2,2]])

m2 = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj2 = TwoDSegmentTree(m2)
obj2.logic()
print obj2.find([[2,1], [4,3]])

