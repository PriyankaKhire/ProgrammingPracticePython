'''
Implement a Queue with help of fix sized arrays.
Such that, if the array runs out of space,
then the queue should duplicate same sized array and keep on adding elements further.
Example:
Q with fixed array size 3
Q
[[None, None, None]]
push(1) push(2) push(3)
Q
[[1,2,3]]
push(4) push(5)
Q
[[1,2,3], [4, 5, None]]

As you can see, initially the queue is made of array with fixed size 3,
as soon as queue runs out of space, it adds another array with size 3 to accomodate new elements
'''
class Array(object):
    def __init__(self, size):
        self.array = [None for i in range(size)]
        self.numElements = 0
        
class Q(object):
    def __init__(self, size):
        self.size = size
        self.arrays = []
        self.head = 0
        self.tail = None

    def push(self, element):
        if(not self.arrays or (self.arrays[-1].numElements == self.size)):
            array = Array(self.size)
            self.arrays.append(array)
            self.tail = 0
        self.arrays[-1].array[self.tail] = element
        self.tail = self.tail + 1
        self.arrays[-1].numElements = self.arrays[-1].numElements + 1
        print [a.array for a in self.arrays]

    def pop(self):
        if(not self.arrays):
            print "Q empty"
            return
        print self.arrays[0].array[self.head]
        self.arrays[0].array[self.head] = None
        self.head = self.head + 1
        self.arrays[0].numElements = self.arrays[0].numElements - 1
        if(self.arrays[0].numElements == 0):
            self.arrays.pop(0)
            self.head = 0
        print [a.array for a in self.arrays]

# Main
obj = Q(3)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(6)
obj.push(7)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.push(8)
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.push(1)
