# LFU Cache
# https://leetcode.com/problems/lfu-cache/
'''
Detailed explanation here:
https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list
'''
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.frequency = 1
        self.next = None
        self.prev = None
        
class DLL(object):
    def __init__(self):
        self.head = Node('head','head')
        self.tail = Node('tail', 'tail')
        self.assignNodesToEachother(self.head, self.tail)

    def assignNodesToEachother(self, head, tail):
        head.next = tail
        tail.prev = head

    def addToTop(self, node):
        nextNode = self.head.next
        # assign head and next node to node
        self.head.next = node
        nextNode.prev = node
        # assign node next and prev to head and next node
        node.prev = self.head
        node.next = nextNode

    def removeNode(self, node):
        nextNode = node.next
        prevNode = node.prev
        # assign the nodes to each other
        self.assignNodesToEachother(prevNode, nextNode)
        # assing node pointers
        node.next = None
        node.prev = None

    def accessNode(self, node):
        self.removeNode(node)
        self.addToTop(node)

    def deleteLastNode(self):
        lastNode = self.tail.prev
        self.removeNode(lastNode)
        return lastNode

    def isEmpty(self):
        if (self.head.next == self.tail):
            return True
        return False

    def display(self):
        ptr = self.head
        while (ptr != None):
            print ptr.key, ptr.val
            ptr = ptr.next
    
class LFUCache(object):

    def __init__(self, capacity):
        print "Created cache with capacity", capacity
        self.capacity = capacity
        self.currSize = 0
        # key = key, val = Node
        self.index = {}
        # key = frequency, val = LRU DLL
        self.frequencyIndex = {}
        self.minFrequency = float('inf')
        """
        :type capacity: int
        """

    def addToFrequencyIndex(self, node):
        dll = None
        # if frequency present in hash
        if (node.frequency in self.frequencyIndex):
            # get the dll
            dll = self.frequencyIndex[node.frequency]
        else:
            # create a dll
            dll = DLL()
            # assing that dll to frequency
            self.frequencyIndex[node.frequency] = dll
        # add node to top of dll
        dll.addToTop(node)
        # update min frequency
        if (self.minFrequency > node.frequency):
            self.minFrequency = node.frequency
        # display dll
        print "displaying dll for frequency", node.frequency
        dll.display()

    def updateValue(self, key, val):
        print "Updating the node value", key, val
        # find the node
        node = self.index[key]
        # update value
        node.val = val
        # remove node from that frequency dll
        dll = self.frequencyIndex[node.frequency]
        dll.removeNode(node)
        # if the dll is empty then delete that frequency
        if (dll.isEmpty()):
            del self.frequencyIndex[node.frequency]
        # if min frequency is current node's frequency then update min frequency
        if (self.minFrequency == node.frequency):
            self.minFrequency = self.minFrequency + 1
        # update current node's frequency
        node.frequency = node.frequency + 1
        # add it to new frequency in frequency index
        self.addToFrequencyIndex(node)

    def removeLeastFrequentlyUsed(self):
        print "Removing least frequently used from frequency", self.minFrequency
        # update current cache size
        self.currSize = self.currSize - 1
        # find least frequently used dll
        lfuDLL = self.frequencyIndex[self.minFrequency]
        print "DLL before deleting last node"
        lfuDLL.display()
        # remove least recently used node
        deletedNode = lfuDLL.deleteLastNode()
        print "DLL after deleting last node", deletedNode.key, deletedNode.val
        lfuDLL.display()
        # if the dll is empty then delete that frequency
        if (lfuDLL.isEmpty()):
            del self.frequencyIndex[self.minFrequency]
        # remove node from index
        del self.index[deletedNode.key]
        # reset min frequency
        self.minFrequency = float('inf')
        

    def addToCache(self, key, val):
        # update current cache size
        self.currSize = self.currSize + 1
        # create node
        node = Node(key, val)
        # add to index
        self.index[key] = node
        # add to frequency index
        self.addToFrequencyIndex(node)
        print "Added new node to cache", key, val
        print "Node index is", self.index
        print "-"*30

    def get(self, key):
        print "Getting key", key
        if not(key in self.index):
            print "key not present"
            return -1
        # get the node
        node = self.index[key]
        # update frequency
        self.updateValue(node.key, node.val)
        return node.val
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        # if key already present then update the value
        if (key in self.index):
            self.updateValue(key, value)
            return
        # if cache is full, remove least frequently used.
        if (self.capacity == self.currSize):
            self.removeLeastFrequentlyUsed()
        self.addToCache(key, value)
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
