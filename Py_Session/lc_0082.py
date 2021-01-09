# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        skip = False
        v = head.val
        fast = head
        slow = ListNode()
        start = slow

        while fast and fast.next:
            hold = fast.next
            if fast.next.val == v:
                skip = True
            else:
                if skip == False:
                    slow.next = fast
                    slow = slow.next
                    slow.next = None
                skip = False
                v = hold.val
            fast = hold
        if skip == False:
            slow.next = fast
        return start.next
