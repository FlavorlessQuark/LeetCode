class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while (head):
            n = head
            head = head.next
            n.next = prev
            prev = n

        return prev
