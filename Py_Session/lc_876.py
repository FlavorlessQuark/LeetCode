class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while 1:
            if not fast.next:
                return slow
            if not fast.next.next:
                return slow.next
            fast = fast.next.next
            slow = slow.next
