#Partition linked list around an element
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
        self.newNode = node()
        self.newNode.setData(data)
        return self.newNode

    def createList(self, n):
        head = node()
        prev = node()
        for i in range(n):
            data = raw_input("Enter data for node ")
            node_i = self.createNode(data)
            if(prev.getData() != None):
                prev.setLink(node_i)
            else:
                head = node_i
            prev = node_i
        return head

    def display(self, head):
        prev = head
        while(prev != None):
            print prev.getData()+"->",
            prev = prev.getLink()
        print "None"

    def partition(self, element, head):
        ptr = head
        prev = ptr
        while(ptr != None):
            if(int(ptr.getData()) < int(element)):
                if(ptr != head):
                    #insert it in front
                    prev.setLink(ptr.getLink())
                    ptr.setLink(head)
                    head = ptr
                    ptr = prev
            prev = ptr        
            ptr = ptr.getLink()
        return head

#Main Program
llist = LinkedList()
head = llist.createList(7)
llist.display(head)
head = llist.partition(5, head)
llist.display(head)
