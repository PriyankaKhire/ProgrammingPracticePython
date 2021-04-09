# LRU Cache
# https://leetcode.com/problems/lru-cache/
'''
Constraints:
1) If the item doesn't exists in cache then put it there
2) If the item is accessed then put it on top
3) If the item exists and we want to update it's value then update the value and put it on top
4) If the cache runs out of capacity then remove the last item and put it on top.
'''
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLL(object):
    def __init__(self, size):
        self.size = size
        self.numberOfNodesCurrentlyPresent = 0
        # Create head and tail
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        # Make them point to each other
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def isCapacity(self):
        if (self.numberOfNodesCurrentlyPresent == self.size):
            return False
        return True
    
    def addToTop(self, node):
        prevNode = self.head
        nextNode = self.head.next
        # Make node point to next and prev
        node.prev = prevNode
        node.next = nextNode
        # Make next and prev point to node
        prevNode.next = node
        nextNode.prev = node
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        # Reassign the pointers
        node.next = None
        node.prev = None
        # Make prev and next point to each other
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def accessNode(self, node):
        self.removeNode(node)
        self.addToTop(node)
    
    def removeLastNode(self):
        lastNode = self.tail.prev
        self.removeNode(lastNode)
        return lastNode
    
    def addNewNode(self, key, val):
        removedNode = None
        newNode = Node(key, val)
        # if cache has capacity to hold nodes
        if (self.numberOfNodesCurrentlyPresent < self.size):
            self.numberOfNodesCurrentlyPresent = self.numberOfNodesCurrentlyPresent + 1
        else:
            removedNode = self.removeLastNode()
        self.addToTop(newNode)
        return newNode, removedNode
    
    def display(self):
        print "Displaying contents of DLL"
        ptr = self.head
        while (ptr != None):
            print ptr.key, ptr.val
            ptr = ptr.next
            
        
class LRUCache(object):

    def __init__(self, capacity):
        self.index = {}
        self.dll = DLL(capacity)
        """
        :type capacity: int
        """
        

    def get(self, key):
        # see if the key is present in hash table or not
        if not(key in self.index):
            return -1
        # if the key is present in hash table then access it
        node = self.index[key]
        self.dll.accessNode(node)
        return node.val
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        # see if the key exists if it does the update the value of the node and move it to top of dll.
        if (key in self.index):
            node = self.index[key]
            node.val = value
            self.dll.accessNode(node)
            return
        # add node to dll
        node, removedNode = self.dll.addNewNode(key, value)
        # add node to index hash table
        self.index[key] = node
        # if any node was removed then remove it from index hash
        if (removedNode != None):
            del self.index[removedNode.key]
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
