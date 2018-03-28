#Circular queue
class circularQ:

    #Add element to q from back and remove from front
    def __init__(self, capacity):
        self.capacity = capacity
        self.q = [None] * capacity
        self.back = 0
        self.front = 0
        self.elementCount = 0

    def isEmpty(self):
        if(self.elementCount == self.capacity):
            return False
        return True
        
    def push(self, value):
        #Check if q is full
        if(not self.isEmpty()):
            print "Q is full"
            return
        #Add the element
        print "Added element "+str(value)
        self.q[self.back] = value
        self.back = (self.back % self.capacity)+1
        if(self.back == self.capacity):
            self.back = 0
        self.elementCount = self.elementCount + 1
        

    def pop(self):
        #Check if q is empty
        if(self.isEmpty()):
            print "Q is empty"
            return
        #Remove element
        print "Removed element "+str(self.q[self.front])
        self.q[self.front] = None
        self.front = (self.front%self.capacity) + 1
        if(self.front == self.capacity):
            self.front = 0
        self.elementCount = self.elementCount - 1

    def display(self):
        print self.q

#Main program
obj1 = circularQ(5)
print obj1.capacity
print obj1.q
obj1.push(1)
obj1.push(2)
obj1.push(3)
obj1.push(4)
obj1.push(5)
obj1.display()
obj1.pop()
obj1.push(6)
obj1.display()
obj1.pop()
obj1.push(7)
obj1.pop()
obj1.push(8)
obj1.pop()
obj1.push(9)
obj1.display()
