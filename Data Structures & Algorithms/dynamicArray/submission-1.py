class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = []

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        # k = self.size
        # self.array.append(-1)
        # while k > i:
        #     self.array[k] = self.array[k-1]
        #     k -= 1
        # self.array[k] = n
        # self.size += 1
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
        self.array.append(n)
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.array.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
