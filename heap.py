#Heap

heap = []

def getParent(index):
    #if odd then left child
    if(index%2 == 1):
        #left child
        return (index-1)/2
    return (index-2)/2

def heapify(index):
    global heap
    #if index out of bounds then return
    if(index <= 0):
        return
    #Compare the value with its parent
    if(heap[getParent(index)] > heap[index]):
        #Return we satisfy the condition
        return
    #Swap
    temp = heap[index]
    heap[index] = heap[getParent(index)]
    heap[getParent(index)] = temp
    #Recurse
    heapify(getParent(index))    

def insert(value):
    global heap
    currIndex = len(heap)
    heap.append(value)
    heapify(currIndex)

#Main
insert(1)
insert(2)
insert(3)
insert(4)
insert(5)
insert(6)
print heap
    
    
