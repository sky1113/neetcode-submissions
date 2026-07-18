class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = low + ((high - low) // 2)
            hours = 0

            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            
            # rate is too low
            if hours > h:
                low = mid + 1
            elif hours <= h:
                high = mid
        
        return low

