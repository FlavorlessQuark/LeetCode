# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traverse = mid = head
        length = 0
        half = 0
        
        while (traverse):
            traverse = traverse.next
            length += 1
            if (((half + 1) < (length)// 2)):
                half += 1
                mid = mid.next

        if (mid.next):
            mid.next = mid.next.next


        if (length == 1):
            head = None
        return head
        # print(length, half, mid.val)
