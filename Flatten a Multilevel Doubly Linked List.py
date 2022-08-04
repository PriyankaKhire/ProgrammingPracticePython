# Flatten a Multilevel Doubly Linked List
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    
    def iterative(self, currPtr):
        stack = []
        while(currPtr):
            # if curr pointer has child then
            if (currPtr.child):
                # if curr pointer has next, add it to stack.
                if (currPtr.next):
                    stack.append(currPtr.next)
                # make child as next pointer to curr pointer
                currPtr.next = currPtr.child
                currPtr.child.prev = currPtr
                currPtr.child = None
            else:
                # if curr pointer doesn't have a child but has a next then go next.
                if currPtr.next:
                    currPtr = currPtr.next
                # if curr pointer doens't have next but stack is not empty then pop top of stack and attach it to current
                elif stack:
                    # pop from top of stack and attach it
                    top = stack.pop()
                    currPtr.next = top
                    top.prev = currPtr
                    currPtr = currPtr.next
                # if stack is also empty and there is no next that means we have reached end of linked list. 
                else:
                    break
        
    def flatten(self, head):
        # self.recurrsive(head)
        self.iterative(head)
        return head
        """
        :type head: Node
        :rtype: Node
        """
        
