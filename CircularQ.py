#Circular Q
class CircularQ(object):
    def __init__(self, size):
        self.size = size
        self.array = [None for i in range(size)]
        self.numElements = 0
        # delete from head
        self.head = 0
        # add from tail
        self.tail = 0

    def push(self, element):
        if(self.numElements == self.size):
            print "Q full"
            return
        self.array[self.tail] = element
        self.tail = (self.tail+1)%self.size
        self.numElements = self.numElements + 1
        print self.array

    def pop(self):
        if(self.numElements == 0):
            print "Q empty"
            return
        print self.array[self.head]
        self.array[self.head] = None
        self.head = (self.head+1)%self.size
        self.numElements = self.numElements - 1
        print self.array

# Main
obj = CircularQ(5)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(6)
obj.pop()
obj.push(6)
obj.push(7)
obj.pop()
obj.push(7)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.push(8)
obj.pop()
obj.push(9)
