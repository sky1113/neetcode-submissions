class MinStack:
    def __init__(self):
        self.vals = []
        self.mins = []

    def push(self, val: int) -> None:
        newMin = val
        if self.mins:
            newMin = min(self.mins[-1], newMin)
        self.vals.append(val)
        self.mins.append(newMin)

    def pop(self) -> None:
        self.vals.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.mins[-1]
