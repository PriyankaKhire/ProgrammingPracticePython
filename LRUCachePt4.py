# LRU Cache
# https://leetcode.com/problems/lru-cache/
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLL(object):
    def __init__(self):
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addFromTop(self, key, val):
        node = Node(key, val)
        nodePrev = self.head
        nodeNext = self.head.next
        node.next = nodeNext
        node.prev = nodePrev
        nodePrev.next = node
        nodeNext.prev = node
        return node
    
    def display(self):
        ptr = self.head
        print "*"*20
        while(ptr):
            print "key", ptr.key, "val", ptr.val
            ptr = ptr.next
        print "*"*20
    
    def deleteNode(self, node):
        nodePrev = node.prev
        nodeNext = node.next
        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev
        del node
    
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        # Key = key, val = node address
        self.index = {}
        self.dll = DLL()
        """
        :type capacity: int
        """
    
    def atCapacity(self):
        if(self.capacity == 0):
            return True
        return False
        

    def get(self, key):
        #print "Called get for key", key
        if not key in self.index:
            return -1
        node = self.index[key]
        newNode = self.update(key, node.val)
        return newNode.val
        """
        :type key: int
        :rtype: int
        """
    
    def update(self, key, value):
        oldNode = self.index[key]
        # delete the node
        self.dll.deleteNode(oldNode)
        # add new from top
        newNode = self.dll.addFromTop(key, value)
        # update index
        self.index[key] = newNode
        return newNode
        
    def evict(self):
        node = self.dll.tail.prev
        self.dll.deleteNode(node)
        del self.index[node.key]
        self.capacity = self.capacity + 1

    def put(self, key, value):
        #print "Put the key val", key, value
        # if the key exists then get it and update it.
        if(key in self.index):
            self.update(key, value)
            return
        # if reached capacity
        if(self.atCapacity()):
            self.evict()
        self.capacity = self.capacity - 1
        # add from top
        newNode = self.dll.addFromTop(key, value)
        # update index
        self.index[key] = newNode
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
