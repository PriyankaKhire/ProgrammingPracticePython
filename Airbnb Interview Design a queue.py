'''
Build a queue class with the enqueue and dequeue methods.
The queue can store an UNLIMITED number of elements.
However, the language you are using has a bug which does not
allow arrays to store more than 5 elements, how would you build that?
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def createNode(self,data):
        return Node(data)

    def addFromTop(self, data):
        node = self.createNode(data)
        if(self.tail == None):
            self.tail = node
        #assign the next ptr, if head is none this shoudn't matter as it gets assigned to none.
        node.next = self.head
        #assign the prev ptr
        if(self.head != None):
            self.head.prev = node
        #move the head ptr upwards
        self.head = node       

    def delFromBottom(self):
        if(self.tail == None):
            return
        #if just one element
        if(self.tail == self.head):
            self.tail = None
            self.head = None
            return
        #Move tail ptr up
        self.tail = self.tail.prev
        #remove the next node reference since we want to delete it.
        self.tail.next = None

    def display(self):
        if(self.head == None):
            print "Queue empty"
            return
        ptr = self.head
        while(ptr):
            print ptr.data,
            ptr = ptr.next
        print "\n"

class Queue(object):
    def __init__(self):
        self.q = LinkedList()

    def push(self, data):
        self.q.addFromTop(data)

    def pop(self):
        self.q.delFromBottom()

    def display(self):
        self.q.display()

#Main
obj = Queue()
obj.push(5)
obj.push(6)
obj.push(7)
obj.push(8)
obj.display()
obj.pop()
obj.display()
obj.pop()
obj.display()
obj.push(9)
obj.display()
obj.pop()
obj.display()
obj.pop()
obj.display()
obj.pop()
obj.display()
obj.pop()
obj.display()
obj.push(1)
obj.display()
obj.push(2)
obj.display()
obj.push(3)
obj.display()
