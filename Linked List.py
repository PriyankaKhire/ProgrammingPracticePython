#Creating a LinkedList

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

    #Creates doubly linked list of n nodes
    def createDoublyLinkedList(self, n):
        prev = node()
        head = node()
        for i in range(n):
            data  = raw_input("Enter data for node:"+str(i)+" \n")
            node_i = self.createNode(data)
            print "Current Node "+str(i)+" contains data = "+str(node_i.getData())
            if(prev.getData() != None):
                print "Previous node contains data = "+str(prev.getData())
                prev.setRlink(node_i)
                node_i.setLlink(prev)
            else:
                head = node_i
            prev = node_i
        return head

#Main Program
llist = LinkedList()
head = llist.createSinglyLinkedList(5)
llist.printList(head)
dhead = llist.createDoublyLinkedList(5)
llist.printList(dhead)
