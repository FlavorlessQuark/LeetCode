class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head
        slow = head

        while (slow.next and fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False
