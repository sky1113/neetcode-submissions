# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = "", ""

        curr1 = l1
        while curr1:
            n1 = str(curr1.val) + n1
            curr1 = curr1.next

        curr2 = l2
        while curr2:
            n2 = str(curr2.val) + n2
            curr2 = curr2.next

        n1, n2 = int(n1), int(n2)
        total = str(n1 + n2)

        head = None

        for n in total:
            newNode = ListNode(int(n), head)
            head = newNode
        
        return head

