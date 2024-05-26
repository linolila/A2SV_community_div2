# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None or node.next is None:
           return
    
        # Copy the value of the next node to the current node
        next_node = node.next
        node.val = next_node.val
        
        # Update the next pointer of the current node to skip the next node
        node.next = next_node.next
        
        # Free the memory occupied by the next node
        next_node = None
