#Merge k sorted Lists
#https://leetcode.com/problems/merge-k-sorted-lists/description/

class MinHeap(object):
    def __init__(self):
        self.array = []

    def isValid(self, index):
        if(index >= 0 and index < len(self.array)):
            return True
        return False

    def getSmallerChildIndex(self, parentIndex):
        leftChildIndex, rightChildIndex = self.getChildern(parentIndex)
        if(self.isValid(leftChildIndex) and self.isValid(rightChildIndex) and (self.array[leftChildIndex] < self.array[rightChildIndex])):
            return leftChildIndex
        return rightChildIndex
    
    def getChildern(self, parent):
        return (2*parent)+1, (2*parent)+2

    def getParent(self, child):
        #if child is odd, it's left child
        if(child%2 == 0):
            return (child-2)/2
        return (child-1)/2

    def push(self, child):
        self.array.append(child)
        #begin comparing to its parents
        childIndex = len(self.array)-1
        parentIndex = self.getParent(childIndex)
        while(self.isValid(parentIndex) and  self.array[parentIndex] > self.array[childIndex]):
            #we swap parent and child
            self.array[parentIndex], self.array[childIndex] = self.array[childIndex], self.array[parentIndex]
            childIndex = parentIndex
            parentIndex = self.getParent(childIndex)

    def pop(self):
        if not self.array:
            return False
        top = self.array[0]
        #put the last element on top
        self.array[0] = self.array.pop()
        parent = 0
        child = self.getSmallerChildIndex(parent)
        while(self.isValid(child) and self.array[parent] > self.array[child]):
            #swap parent and child
            self.array[parent], self.array[child] = self.array[child], self.array[parent]
            parent = child
            child = self.getSmallerChildIndex(parent)
        return top

    def displayHeap(self):
        print self.array

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class HeapApproch(object):
    def __init__(self, lists):
        self.lists = lists
        self.h = MinHeap()
        self.answerRoot = None
        self.answerTail = None

    def createNode(self, val):
        node = ListNode(val)
        return node

    def sol(self):
        #create a heap of k size
        for lst in self.lists:
            self.h.push(lst.pop(0))
        while(self.lists):
            for i in range(len(self.lists)):
                #Pop the list thats empty
                #incomplete, complete it here
                if not self.lists[i]:
                    self.lists.pop(i)
                    continue
                top = self.h.pop()
                self.h.push(self.lists[i].pop(0))
                if top:
                    topNode = self.createNode(top)
                    print top
                    if self.answerRoot == None:
                        self.answerRoot = topNode
                    else:
                        self.answerTail.next = topNode
                    self.answerTail = topNode
                        


#Main
o = HeapApproch([[1,4,5],[1,3,4],[2,6]])
o.sol()
