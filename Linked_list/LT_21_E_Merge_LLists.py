# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        l1, l2 = list1, list2


        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next

def main():
    list1 = [1,2,4]
    list2 = [1,3,5]
    res = Solution()
    print(res.mergeTwoLists(list1, list2))

if __name__ == "__main__":
    main()