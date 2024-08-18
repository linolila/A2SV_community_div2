# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node just before the left position
        for _ in range(left - 1):
            prev = prev.next
        
        # Start reversing the sublist
        curr = prev.next
        next_node = None
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next