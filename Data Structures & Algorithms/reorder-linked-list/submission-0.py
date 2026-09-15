# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # split lists
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail1 = slow
        slow = slow.next
        tail1.next = None

        # reverse second half
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #  merge list2 into list 1
        list1, list2 = head, prev
        while list2:
            tmp1, tmp2 = list1.next, list2.next
            list2.next = list1.next
            list1.next = list2
            list1, list2 = tmp1, tmp2
        

        


