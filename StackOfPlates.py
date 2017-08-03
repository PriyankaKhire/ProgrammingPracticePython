 #Imagine a (literal) stack of plates. If the stack gets too high, it
 # might topple. Therefore, in real life, we would likely start a new
 # stack when the previous stack exceeds some threshold. Implement a
 # data structure SetOfStacks that mimics this. SetOfStacks should be
 # composed of several stacks and should create a new stack once the
 # previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
 # should behave identically to a single stack (that is, pop() should
 # return the same values as it would if there were just a single stack).
 #
 # FOLLOW UP
 # Implement a function popAt(int index) which performs a pop operation
 # on a specific sub-stack.

class node():
    def __init__(self):
        self.data = None
        self.downLink = None
        self.upLink = None
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setDownLink(self, link):
        self.downLink = link
    def getDownLink(self):
        return self.downLink
    def setUpLink(self, link):
        self.upLink = link
    def getUpLink(self):
        return self.upLink

class stackOfPlates():
    def __init__(self, stackCapacity):
        #Holds the bottom elements of the stack, this variable can be deleted.
        self.bottom = []
        #Holds the remaining capacity at a given index
        self.capacity = []
        #Holds the top emement of the stacks
        self.top = []
        #Tells the capacity of the current stack
        self.stackCapacity = stackCapacity
        
    def createNode(self, data):
        newNode = node()
        newNode.setData(data)
        return newNode

    def pop(self):
        if not self.bottom:
            print "Stack empty"
            return
        #Get top element of the last stack
        top_element = self.top[-1]
        #replace this element with next element
        #if popping this makes the current stack empty
        if top_element.upLink == None:
            self.top[:-1]
            self.capacity[:-1]
            self.bottom[:-1]
        else:
            self.top[-1] = top_element.upLink
            self.capacity[-1] -= 1
            top_element.getUpLink().setDownLink(None)
        print "Deleted "+str(top_element.getData())

    def push(self, data):
        obj = self.createNode(data)
        #We need to find it a place
        #If the latest stack capacity is excedeed or if this is the first item to be pushed
        if ( not self.bottom) or (self.capacity[:-1] == self.stackCapacity):
            #Make a new stack
            self.bottom.append(obj)
            self.top.append(obj)
            self.capacity.append(1)
            print self.bottom
        else:
            self.top[-1].setDownLink(obj)
            obj.setUpLink(self.top[-1])
            self.top[-1] = obj
            self.capacity[-1] += 1
            print self.top
        print "Pushed "+str(data)

    def display(self):
        for stack in self.bottom:
            print stack.getData()
        print self.bottom
            
 #Main Program
s = stackOfPlates(2)
s.push(1)
s.push(1)
s.push(2)
s.push(2)
s.push(3)
s.display()


#Here is the idea on how to do this
#First have an array hold the bottom elements of all the stacks
#Another array hold the top elements of all the stacks
#Another array holds the number of elements in each stack
#Have these arrays hold double ended linked list
#It would look something like this
#bottom[node.element1.1, node.element2.1, node.element3.1]
#               ||                      ||                          ||
#           node.element1.2   node.element2.2   node.element3.1
#               ||                      ||                          ||
#top     [node.element1.3, node.element2.3, node.element3.3]
#When ever something is popped or pushed then replace the top array elements.
