class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            
            d = math.sqrt(x**2 + y**2)
            heapq.heappush_max(heap, (d, [x, y]))

            while len(heap) > k:
                heapq.heappop_max(heap)
        
        for i in range(len(heap)):
            heap[i] = heap[i][1]

        return heap

