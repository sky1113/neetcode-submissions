class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None


    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = self.Node(val)

        if self.size:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = self.Node(val)

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            
            newNode = self.Node(val)

            prev = curr.prev
            nxt = curr
            prev.next = newNode
            newNode.prev = prev
            newNode.next = nxt
            nxt.prev = newNode

            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        elif index == 0:
            newHead = self.head.next
            newHead.prev = None
            self.head = newHead
        elif index == self.size - 1:
            newTail = self.tail.prev
            newTail.next = None
            self.tail = newTail
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            
            prev = curr.prev
            nxt = curr.next
            prev.next = nxt
            nxt.prev = prev

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)