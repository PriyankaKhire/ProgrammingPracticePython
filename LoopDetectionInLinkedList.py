#Loop detection in Linked List
import random

class node:
    def __init__(self):
        self.data = None
        self.rlink = None
        self.llink = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def setRlink(self, link):
        self.rlink = link

    def getRlink(self):
        return self.rlink

    def setLlink(self, link):
        self.llink = link

    def getLlink(self):
        return self.llink

class LinkedList:

    #Create Node and assign it data
    def createNode(self, data):
        self.newNode = node()
        self.newNode.setData(data)
        return self.newNode

    #Creates singly linked list of n nodes
    def createSinglyLinkedList(self, n):
        prev = node()
        head = node()
        for i in range(n):
            data  = raw_input("Enter data for node:"+str(i)+" \n")
            node_i = self.createNode(data)
            print "Current Node "+str(i)+" contains data = "+str(node_i.getData())
            if(prev.getData() != None):
                print "Previous node contains data = "+str(prev.getData())
                prev.setRlink(node_i)
            else:
                head = node_i
            prev = node_i
        return head
    
    #Prints the linked list
    def printList(self, head_node):
        ptr = node()
        ptr = head_node
        print "\nThe entire list is:"
        while(ptr != None):
            print ptr.getData()+"->",
            ptr = ptr.getRlink()
        print "None"

    #This function adds loop at a random place in the linked list
    def addLoop(self, head):
        #get the size of the list and come to last node of linked list
        end = head
        size = 0
        while(end.getRlink() != None):
            size += 1
            end = end.getRlink()
        #Select random node to be the loop head
        loop_node = random.randint(0, size)
        curr_ptr = head
        count = 0
        while(curr_ptr != None):
            count +=1
            if(count == loop_node):
                end.setRlink(curr_ptr)
                break
            curr_ptr = curr_ptr.getRlink()
        print "Loop head is "+end.getRlink().getData()
        return head

    #this function detects if the list has loop or not with help of rabbit and tortoise
    def detectLoop(self, head):
        rabbit = head
        tortoise = head
        while(rabbit != None):
            tortoise = tortoise.getRlink()
            rabbit = rabbit.getRlink()
            if(rabbit != None):
                rabbit = rabbit.getRlink()
            if(rabbit == tortoise):
                print "There is a loop in the linked list"
                self.findLoopHead(head, rabbit)
                return True
        print "There is no loop in the linked list"
        return False

    #This function gives the head of the loop in linked list
    def findLoopHead(self, head, meetNode):
        while(head != meetNode):
            head = head.getRlink()
            meetNode = meetNode.getRlink()
        print "head of the loop is at "+head.getData()


#Main Program
ll = LinkedList()
h = ll.createSinglyLinkedList(5)
ll.printList(h)
h = ll.addLoop(h)
print ll.detectLoop(h)
h2 = ll.createSinglyLinkedList(5)
ll.printList(h2)
print ll.detectLoop(h2)
