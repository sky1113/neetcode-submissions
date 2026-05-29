class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        print(self.heap)
        return sorted(self.heap, reverse = True)[self.k - 1]
