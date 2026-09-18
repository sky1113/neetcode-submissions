class BrowserHistory:

    class Node:
        
        def __init__(self, url):
            self.url = url
            self.prev = None
            self.next = None

    def __init__(self, homepage: str):
        newNode = self.Node(homepage)
        self.head = newNode
        self.tail = newNode
        self.curr = newNode

    def visit(self, url: str) -> None:
        newNode = self.Node(url)

        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = newNode
        self.tail = newNode

    def back(self, steps: int) -> str:
        while steps > 0:
            if self.curr == self.head:
                return self.head.url
            else:
                self.curr = self.curr.prev
                steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.curr == self.tail:
                return self.tail.url
            else:
                self.curr = self.curr.next
                steps -= 1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)