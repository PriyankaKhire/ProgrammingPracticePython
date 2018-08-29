#Merge k Sorted Lists
#https://leetcode.com/problems/merge-k-sorted-lists/description/
import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class LinkedList(object):
    def __init__(self, l):
        self.list = l
        self.root = None
        self.tail = None

    def createNode(self, val):
        node = ListNode(val)
        return node

    def addNext(self, parent, child):
        parent.next = child

    def createList(self):
        for element in self.list:
            #create Node
            node = self.createNode(element)
            if (self.root == None):
                self.root = node
            else:
                self.addNext(self.tail, node)
            self.tail = node
                
                

class Solution(object):
    def __init__(self):
        self.listTop = []
        self.heap = []
        self.activeLists = 0
    
    def push(self, node, listIndex):
        heapq.heappush(self.heap, [node.val,listIndex])
    
    def pop(self):
        return heapq.heappop(self.heap)
    
    def isListsEmpty(self):
        if(self.activeLists > 0):
            return False
        return True
    
    def incrementList(self, listIndex):
        self.listTop[listIndex] = self.listTop[listIndex].next
        if not(self.listTop[listIndex]):
            self.activeLists = self.activeLists - 1
        
    def mergeKLists(self, lists):
        if not lists:
            return
        
        #clean lists
        ls = []
        for i in range(len(lists)):
            if (lists[i]):
                ls.append(lists[i])
        
        if not ls:
            return
        
        lists = ls
        
        #put top of lists in list Heads
        for l in lists:
            self.listTop.append(l)
        
        output = []
        self.activeLists = len(lists)
        
        #create initial heap
        for i in range(len(self.listTop)):
            self.push(self.listTop[i], i)
            self.incrementList(i)
        
        #now start merging
        while not(self.isListsEmpty()):
            #pop from heap
            elementAndList = self.pop()
            e = elementAndList[0]
            l = elementAndList[1]
            #Add to output
            output.append(e)
            #Add element to heap
            if(self.listTop[l]):
                self.push(self.listTop[l], l)
                self.incrementList(l)
        
        #add remaining elements of list
        while(self.heap):
            elementAndList = self.pop()
            e = elementAndList[0]
            #Add to output
            output.append(e)
        print output

#Main Program
l1 = LinkedList([1,4,5])
l2 = LinkedList([1,3,4])
l3 = LinkedList([2,6])
s = Solution()
s.mergeKLists([l1.root,l2.root,l3.root])
