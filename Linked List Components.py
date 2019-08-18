# Linked List Components
# https://leetcode.com/problems/linked-list-components/
'''
Thoughts:
the discription is misleading. I solved for a different problem that I understood.
Thus it does not pass all test case.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.hash = {}
        
    def putInHash(self, G):
        for element in G:
            self.hash[element] = False
        self.hash[None] = False
    
    def checkIfComponentsInHash(self, component, nextComponent):
        if(component.val in self.hash and self.hash[component.val] == False):
            if(nextComponent == None and self.hash[None] == False):
                self.hash[component.val] = True
                self.hash[None] = True
                return True
            elif(nextComponent.val in self.hash and self.hash[nextComponent.val] == False):
                self.hash[component.val] = True
                self.hash[nextComponent.val] = True
                return True
        return False
    
    def goOverLinkedList(self, head):
        ptr = head
        connectedComponent = 0
        while(ptr):
            if(self.checkIfComponentsInHash(ptr, ptr.next)):                
                connectedComponent = connectedComponent + 1                    
            ptr = ptr.next
        # see if head has been involved in a component match already else pair it with None->head
        if(head.val in self.hash and self.hash[head.val] == False):
            connectedComponent = connectedComponent + 1
        return connectedComponent
                
        
    def numComponents(self, head, G):
        self.putInHash(G)
        return self.goOverLinkedList(head)
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        
