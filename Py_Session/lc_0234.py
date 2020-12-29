# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l1 = head
        l2 = head

        if not head or not head.next:
            return True
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next

        mid = []
        while l1:
            mid.append(l1.val)
            l1 = l1.next

        while mid:
            if mid[-1] != head.val:
                return False
            head = head.next
            mid.pop()
        return True
