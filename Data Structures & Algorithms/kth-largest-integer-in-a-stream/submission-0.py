class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.heap.sort(reverse = True)
        self.index = k

    def add(self, val: int) -> int:
        self.heap.append(val)
        self.heap.sort(reverse = True)
        print(self.heap)
        return self.heap[self.index - 1]
