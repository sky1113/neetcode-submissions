"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # iterate through twice
        # once to create node copies and next chain, again to copy random pointers
        nodeMap = {None: None}

        dummy = curr2 = Node(0)
        curr1 = head
        while curr1:
            tmp = Node(curr1.val)
            nodeMap[curr1] = tmp
            curr2.next = tmp
            curr2 = curr2.next
            curr1 = curr1.next
        
        head2 = dummy.next
        curr1, curr2 = head, head2

        while curr1:
            curr2.random = nodeMap[curr1.random]
            curr1, curr2 = curr1.next, curr2.next
        
        return head2

        