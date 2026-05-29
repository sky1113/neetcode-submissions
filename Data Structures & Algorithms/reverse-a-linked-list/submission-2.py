# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        if curr == None or curr.next == None:
            return curr

        while curr.next != None:
            if prev == None:
                prev = curr
                curr = curr.next
                prev.next = None
                continue
            temp = prev
            prev = curr
            curr = curr.next
            prev.next = temp

        curr.next = prev

        return curr