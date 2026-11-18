class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head is None

    def append(self, value: int) -> None:
        if self.tail:
            self.tail.next = Node(value, self.tail)
            self.tail = self.tail.next
        else:
            self.tail = self.head = Node(value)
        
    def appendleft(self, value: int) -> None:
        if self.head:
            self.head.prev = Node(value, None, self.head)
            self.head = self.head.prev
        else:
            self.tail = self.head = Node(value)
        
    def pop(self) -> int:
        if self.tail:
            temp = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return temp.val
    
        else: return -1
        

    def popleft(self) -> int:
        if self.head:
            temp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return temp.val
        
        else: return -1
