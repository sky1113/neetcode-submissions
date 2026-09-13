# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        res = None
        tail = None

        while list1 or list2:
            if not list1:
                tail.next = list2
                return res
            if not list2:
                tail.next = list1
                return res
            
            if list1.val <= list2.val:
                curr = list1
                list1 = list1.next
            else:
                curr = list2
                list2 = list2.next

            curr.next = None

            if not res:
                res = curr
                tail = curr
            else:
                tail.next = curr
                tail = curr
        
        return res


