# Design Browser History
# https://leetcode.com/problems/design-browser-history/
class Node(object):
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None
        
class DLL(object):
    def __init__(self, homepage):
        self.head = Node('head')
        self.tail = Node(homepage)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.currPtr = self.tail
    
    def addFromTop(self, url):
        node = Node(url)
        prevNode = self.head
        nextNode = self.head.next
        prevNode.next = node
        nextNode.prev = node
        node.next = nextNode
        node.prev = prevNode
        # Make curr pointer point to that node.
        self.currPtr = node
    
    def moveBack(self, steps):
        while (self.currPtr != self.tail and steps > 0):
            steps = steps - 1
            self.currPtr = self.currPtr.next
    
    def moveForward(self, steps):
        while (self.currPtr.prev != self.head and steps > 0):
            steps = steps - 1
            self.currPtr = self.currPtr.prev
    
    def clearForwardHistory(self):
        self.head.next = self.currPtr
        self.currPtr.prev = self.head
    
    
    
class BrowserHistory(object):

    def __init__(self, homepage):
        self.dll = DLL(homepage)
        """
        :type homepage: str
        """
        

    def visit(self, url):
        self.dll.clearForwardHistory()
        self.dll.addFromTop(url)
        """
        :type url: str
        :rtype: None
        """
        

    def back(self, steps):
        self.dll.moveBack(steps)
        return self.dll.currPtr.url
        """
        :type steps: int
        :rtype: str
        """
        

    def forward(self, steps):
        self.dll.moveForward(steps)
        return self.dll.currPtr.url
        """
        :type steps: int
        :rtype: str
        """
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
