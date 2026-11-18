class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.tail = 0

    def visit(self, url: str) -> None:
        try:
            self.history[self.curr + 1] = url
        except:
            self.history.append(url)
        self.curr += 1
        self.tail = self.curr

    def back(self, steps: int) -> str:
        new = self.curr - steps
        if new < 0:
            new = 0
        self.curr = new
        return self.history[new]
        
    def forward(self, steps: int) -> str:
        new = self.curr + steps
        if new > self.tail:
            new = self.tail
        self.curr = new
        return self.history[new]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)