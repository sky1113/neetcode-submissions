class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if not curr:
            return -1
        else:
            return curr.val
        
    def insertHead(self, val: int) -> None:
        if self.head:
            node = Node(val, self.head)
            self.head = node
        else:
            self.head = self.tail = Node(val)

    def insertTail(self, val: int) -> None:
        if self.tail:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        else:
            self.head = self.tail = Node(val)

    def remove(self, index: int) -> bool:
        prev = Node(-1, self.head)
        curr = self.head
        while curr and index > 0:
            prev = curr
            curr = curr.next
            index -= 1
        if not curr: return False

        # edge cases, ll 1 long & i == 0, 
        if curr == self.head and curr == self.tail:
            self.head = None
            self.tail = None
        elif curr == self.head:
            self.head = self.head.next
        elif curr == self.tail:
            self.tail = prev
        
        prev.next = curr.next
        return True
    
    def getValues(self) -> List[int]:
        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
