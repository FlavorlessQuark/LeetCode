# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        result = head
        remainder = 0
        while l1 or l2:
            v1 = 0
            v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            addition = v1 + v2 + remainder
            remainder = 0
            if addition >= 10:
                remainder = 1
                addition -= 10
            result.next = ListNode(addition)
            result = result.next
        if remainder == 1:
            result.next = ListNode(1)
        return head.next
