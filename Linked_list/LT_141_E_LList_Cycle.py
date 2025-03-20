# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
def main():
    head = [1,2,3,4]
    index = 1
    res = Solution()
    print(res.hasCycle(head))

if __name__ == "__main__":
    main()