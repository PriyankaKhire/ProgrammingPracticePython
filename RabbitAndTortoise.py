#Rabbit and hare
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
        prev = node()
        prev = head
        while(prev != None):
            print prev.getData()+"->",
            prev = prev.getLink()
        print "None"

    def findMid(self, head):
        rabbit = node()
        tortoise = node()
        rabbit = head
        tortoise = head
        while(rabbit.getLink() != None):
            rabbit = rabbit.getLink()
            tortoise = tortoise.getLink()
            if(rabbit != None):
                rabbit = rabbit.getLink()
        print "Mid is = "+str(tortoise.getData())

#Main Program
llist = LinkedList()
list1 = llist.createList(5)
llist.display(list1)
llist.findMid(list1)
