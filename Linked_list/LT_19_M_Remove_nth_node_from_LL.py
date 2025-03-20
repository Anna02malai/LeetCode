# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Use 2 ptrs 
        dummy = ListNode(0, head)
        l = dummy
        r = head

        # Offset the ptrs by n nodes
        for i in range(n):
            r = r.next
        
        # Iterate the ptrs to find the node to be deleted
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        return dummy.next

        