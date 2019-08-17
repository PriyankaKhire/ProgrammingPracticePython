# Delete all odd or even positioned nodes from Circular Linked List
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.root = None

    def createNode(self, data):
        return Node(data)

    def createNLinkedList(self, n):
        self.root = self.createNode(0)
        ptr = self.root
        for i in range(1, n):
            node = self.createNode(i)
            ptr.next = node
            ptr = node
        return ptr

    def createNCircularLinkedList(self, n):
        tail = self.createNLinkedList(n)
        # Make it circular
        tail.next = self.root
        

    def display(self):
        print self.root.data, "->",
        ptr = self.root.next
        while(ptr != self.root):
            print ptr.data,"->",
            ptr = ptr.next
        print "root"

class DeleteNodes(object):
    
    def deleteOddNodes(self, linkedList):
        # this function needs at least 3 nodes in our linked list, so have edge cases to delete 1 and 2 nodes
        prev = linkedList.root
        ptr = linkedList.root.next
        count = 1
        while(ptr != linkedList.root):
            print "Count",count
            if(count%2 == 1):
                print "deleting current node",ptr.data
                prev.next = ptr.next
            else:
                print "Not deleting this node"
                prev = ptr
            ptr = ptr.next
            count = count + 1

    def deleteEvenNodes(self, linkedList):
        # this function needs at least 3 nodes in our linked list, so have edge cases to delete 1 and 2 nodes
        prev = linkedList.root.next
        ptr = prev.next
        count = 2
        while(ptr != linkedList.root):
            print "Count",count
            if(count%2 == 0):
                print "Deleting current node", ptr.data
                prev.next = ptr.next
            else:
                print "Not deleting this node"
                prev = ptr
            ptr = ptr.next
            count = count + 1
        print "Deleting the root", linkedList.root.data
        # delete the root coz it's at even number
        # your prev is gonna be the tail
        prev.next = ptr.next
        linkedList.root = ptr.next
                
            

# Main
ll = LinkedList()
ll.createNCircularLinkedList(10)
ll.display()
obj = DeleteNodes()
obj.deleteEvenNodes(ll)
ll.display()
