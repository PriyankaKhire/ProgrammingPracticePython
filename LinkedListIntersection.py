#Intersection of 2 linked list
import random
class node():
    def __init__(self):
        self.data = None
        self.link = None
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setLink(self, link):
        self.link = link
    def getLink(self):
        return self.link

class LinkedList():
    def createNode(self, data):
        newNode = node()
        newNode.setData(data)
        return newNode
    #Creates 2 intersecting linked lists 1 of length n and other of length m+n-rand
    def createIntersectingLinkedList(self,n, m):
        head_n = None
        prev = None
        intersecting_node = random.randint(0, n)
        print "For first list"
        for i in range(n):
            data = raw_input("Enter data for node "+str(i)+" ")
            node_i = self.createNode(data)
            if(head_n == None):
                head_n = node_i
            if(prev != None):
                prev.setLink(node_i)
            prev = node_i
            if i == intersecting_node:
                intersecting_node = node_i
        prev = None
        head_m = None
        print "For second list"
        for j in range(m):
            data = raw_input("Enter data for node "+str(j)+" ")
            node_j = self.createNode(data)
            if(head_m == None):
                head_m = node_j
            if(prev != None):
                prev.setLink(node_j)
            prev = node_j
            if( j == m-1):
                node_j.setLink(intersecting_node)
        return head_n, head_m
               
    def display(self, head):
        ptr = head
        while(ptr != None):
            print ptr.getData()+"->",
            ptr = ptr.getLink()
        print "None"

    def findIntersectingWithHash(self, head_n, head_m):
        hash_table = {}
        #Traverse first list and put it in hash table
        ptr = head_n
        while(ptr != None):
            hash_table[ptr] = True
            ptr = ptr.getLink()
        #Traverse the second list
        ptr = head_m
        while(ptr != None):
            if(ptr in hash_table):
                print "Found the intersecting node "+str(ptr.getData())
                break
            ptr = ptr.getLink()
        self.display(head_n)
        self.display(head_m)

    def findIntersectingWithNodeCounting(self, head_n, head_m):
        #Count nodes in first list
        count_n = 0
        ptr = head_n
        while(ptr != None):
            count_n +=1
            ptr = ptr.getLink()
        #Count nodes in second list
        count_m = 0
        ptr = head_m
        while(ptr != None):
            count_m += 1
            ptr = ptr.getLink()
        #Compare
        if(count_m < count_n):
            big = head_n
            small = head_m
            diff = count_n - count_m
        else:
            big = head_m
            small = head_n
            diff = count_m - count_n
        #Move big, diff nodes ahead
        ptr = big
        count = 0
        while(ptr != None and count < diff):
            count +=1
            ptr = ptr.getLink()
        #Now traverse both of them together
        ptr_small = small
        while(ptr != None and ptr_small != None):
            if(ptr == ptr_small):
                print "found intersecting node "+ptr.getData()
                break
            ptr = ptr.getLink()
            ptr_small = ptr_small.getLink()
        self.display(head_n)
        self.display(head_m)
            

#Main Program
ll = LinkedList()
n, m = ll.createIntersectingLinkedList(5,3)
ll.findIntersectingWithHash(n, m)
ll.findIntersectingWithNodeCounting(n,m)
