# How to heap sort on particular attribute of an object
# in python 2 we use __cmp__ method to do that and tell to compare that attribute.
import heapq

class SomeClass(object):
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def __cmp__(self, otherObject):
        return cmp(self.attribute2, otherObject.attribute2)

class HeapClass(object):
    def __init__(self):
        self.list1 = [2,10,3,1,5,8]
        self.list2 = [5,4,3,9,7,2]
        #Create some class objects
        heapOfSomeClassObjects = []
        for i in range(len(self.list1)):
            obj = SomeClass(self.list1[i], self.list2[i])
            # heap push
            heapq.heappush(heapOfSomeClassObjects, obj)
        #print sorted heap, by popping it (remember just printing it won't give you sorted result it's a heap
        while(heapOfSomeClassObjects):
            someObject = heapq.heappop(heapOfSomeClassObjects)
            print someObject.attribute2

# Main
obj = HeapClass()

 
