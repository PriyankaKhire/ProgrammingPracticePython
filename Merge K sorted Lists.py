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
        #if one child is valid and other is not
        if(self.isValid(leftChildIndex) and not self.isValid(rightChildIndex)):
            return leftChildIndex
        elif(self.isValid(rightChildIndex) and not self.isValid(leftChildIndex)):
            return rightChildIndex
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
        if len(self.array) == 1:
            return self.array.pop()
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

#This object helps us to keep track of top pointer of the lists
class qObject(object):
    def __init__(self, lst, ptr):
        self.list = lst
        self.ptr = ptr

class HeapApproch(object):
    def __init__(self, lists):
        self.lists = lists
        self.h = MinHeap()
        self.answerRoot = None
        self.answerTail = None

    def createNode(self, val):
        node = ListNode(val)
        return node

    def createLinkedList(self, val):
        print val

    def sol(self):
        q = []
        #create heap of k nodes and simultaneously create qObjects for lists
        for l in self.lists:
            #add to heap
            self.h.push(l[0])
            #create qObject for the list and add it to q
            qo = qObject(l, 1)
            q.append(qo)
        #while the q is not empty
        while q:
            #pop the item
            top = q.pop(0)
            if(top.ptr < len(top.list)):
                #pop from heap
                val = self.h.pop()
                #send value to make linked list
                self.createLinkedList(val)
                self.h.push(top.list[top.ptr])
                top.ptr = top.ptr+1
                q.append(top)
        #remove remaining elements in heap
        while self.h.array:
            val = self.h.pop()
            self.createLinkedList(val)
                
        


#Main
o = HeapApproch([[1,4,5],[1,3,4],[2,6]])
o.sol()
