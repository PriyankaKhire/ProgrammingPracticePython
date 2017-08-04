#heap
#This is a max heap
class heap():
    def __init__(self):
        self.heapArray = []
    def displayHeapArray(self):
        print self.heapArray
    def getLeftChildIndex(self, root):
        return (2*root)+1
    def getRightChildIndex(self, root):
        return (2*root)+2
    def getParentIndex(self, child):
        if(child%2 == 1):
            #Left child
            return (child-1)/2
        return (child-2)/2
    def bottomHeapify(self, childIndex):
        if(childIndex != 0):
            #Get parent index
            parentIndex = self.getParentIndex(childIndex)
            #Check if the parent is small
            if(self.heapArray[parentIndex] < self.heapArray[childIndex]):
                #Swap parent and child
                self.heapArray[parentIndex], self.heapArray[childIndex] = self.heapArray[childIndex], self.heapArray[parentIndex]
                self.bottomHeapify(parentIndex)
                
    def add(self, data):
        self.heapArray.append(data)
        self.bottomHeapify(len(self.heapArray)-1)
        self.displayHeapArray()

    def topHeapify(self, parentIndex):
        if(parentIndex < len(self.heapArray)):
            #Find childern
            rChild = self.getRightChildIndex(parentIndex)
            lChild = self.getLeftChildIndex(parentIndex)
            #If the childern are in bound
            if(rChild < len(self.heapArray) and lChild < len(self.heapArray)):
                #Find bigger child
                if(self.heapArray[rChild] > self.heapArray[lChild]):
                    #Swap with r child
                    self.heapArray[rChild], self.heapArray[parentIndex] = self.heapArray[parentIndex], self.heapArray[rChild]
                    self.topHeapify(rChild)
                else:
                    #Swap with l child
                    self.heapArray[lChild], self.heapArray[parentIndex] = self.heapArray[parentIndex], self.heapArray[lChild]
                    self.topHeapify(lChild)
            
    def remove(self):
        if not self.heapArray:
            print "Heap is empty"
            return
        print "Removed element "+str(self.heapArray[0])
        self.heapArray[0] = self.heapArray[-1]
        del self.heapArray[-1]
        self.topHeapify(0)
        self.displayHeapArray()

#Main Program
h = heap()
h.add(5)
h.add(6)
h.add(7)
h.remove()
h.add(8)
h.remove()
h.remove()
h.remove()
h.remove()
