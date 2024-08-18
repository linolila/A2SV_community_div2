# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))
        curr = head
        
        while curr:
            # At each step, remove `curr` from the original list
            prev = dummy
            # Find the correct place to insert `curr` in the sorted list
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert `curr` into the sorted list
            next_node = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next_node
        
        return dummy.next
