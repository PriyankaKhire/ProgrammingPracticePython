#Heap

heap = []

def getParent(index):
    #if odd then left child
    if(index%2 == 1):
        #left child
        return (index-1)/2
    return (index-2)/2

def getGreaterKid(index):
    global heap
    #left
    l = (2*index)+1
    #right
    r = (2*index)+2
    #child index out of bounds
    if(l >= len(heap) or r >= len(heap)):
        return -1
    if heap[l] > heap[r]:
        return l
    return r
    
def bottom_heapify(index):
    global heap
    #if index is out of bounds
    if(index >= len(heap)):
        return
    child = getGreaterKid(index)
    if(child == -1):
        return
    #if greater child is greater than parent then recurse
    if(heap[child] < heap[index]):
        #return
        return
    #Swap
    temp = heap[index]
    heap[index] = heap[child]
    heap[child] = temp
    #Recurse
    bottom_heapify(child)
    

def top_heapify(index):
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
    top_heapify(getParent(index))    

def insert(value):
    global heap
    currIndex = len(heap)
    heap.append(value)
    top_heapify(currIndex)

def delete():
    #delete the head value and replace it with top value
    if not heap:
        return
    heap[0] = heap.pop()
    bottom_heapify(0)

#Main
insert(1)
insert(2)
insert(3)
insert(4)
insert(5)
insert(6)
delete()
delete()
insert(7)
print heap
    
    
