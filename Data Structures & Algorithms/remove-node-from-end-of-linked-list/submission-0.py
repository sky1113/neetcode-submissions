# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        sz = 0
        while curr:
            curr = curr.next
            sz += 1

        i = sz - n
        if i == 0:
            return head.next

        prev, curr = None, head
        while i > 0:
            prev = curr
            curr = curr.next
            i -= 1
        
        prev.next = curr.next
        return head
        
