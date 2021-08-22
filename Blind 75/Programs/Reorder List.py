# Reorder List
# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def detachInMiddle(self, head):
        rabbit = head
        tortoise = head
        # move rabbit 1X times and rabbit 2X times. This will make sure tortoise is in the middle of list by the time rabbit reaches the end of the list.
        while(rabbit):
            rabbit = rabbit.next
            if (rabbit and rabbit.next):
                rabbit = rabbit.next
                tortoise = tortoise.next
        # now toroise is in the middle
        newHead = tortoise.next
        # detach the lists
        tortoise.next = None
        return head, newHead
    
    # Detach the nodes of the list and put it in stack.
    def putListInStack(self, root):
        stack = []
        while(root):
            # add node to stack
            stack.append(root)
            # assign current node to previous node
            prevNode = root
            # move the current node to next position
            root = root.next
            # detach the previous node from the list
            prevNode.next = None
        return stack
    
    def attachStackNodesToList(self, l1, stack):
        # assign pointer to head of list 1
        ptr = l1
        while(stack):
            # pop the top of stack
            top = stack.pop()
            # assign previous and next nodes
            prevNode = ptr
            nextNode = ptr.next
            # concatinate top node in between previous and next nodes.
            prevNode.next = top
            top.next = nextNode
            # advance the ptr
            ptr = nextNode
            
    def reorderList(self, head):
        # detach the list in middle.
        l1, l2 = self.detachInMiddle(head)
        # put l2 in stack, this helps in reversing the list
        stack = self.putListInStack(l2)
        # attach stack nodes to the list 1
        self.attachStackNodesToList(l1, stack)
        return l1
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
