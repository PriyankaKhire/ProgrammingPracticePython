# LRU Cache
#https://leetcode.com/problems/lru-cache/
class DLLNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class DLLStack(object):
    def __init__(self):
        self.top = None
        self.bottom = None

    def createNode(self, key, value):
        return DLLNode(key, value)

    def addFromTop(self, key, value):
        node = self.createNode(key, value)
        if(self.top != None):
            node.previous = self.top
            self.top.next = node
        if(self.top == None):
            self.bottom = node
        self.top = node

    def deleteFromBottom(self):
        if(self.bottom == None):
            return
        if(self.bottom == self.top):
            self.top = None
            self.bottom = None
            return
        #Assign new bottom
        self.bottom = self.bottom.next
        #remove pointer from the top node of our current bottom node
        self.bottom.previous = None
        
    def display(self):
        ptr = self.top
        while(ptr != None):
            print ptr.data,
            ptr = ptr.previous
        print ""

        
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.index = {}
        self.dllQ = DLLStack()
        """
        :type capacity: int
        """
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#Main
#obj = LRUCache()
