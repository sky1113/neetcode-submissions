class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currAvg = 0
        count = 0
        L = 0

        for R in range(len(arr)):
            currAvg += (arr[R] / k)
            if R - L + 1 == k:
                if currAvg >= threshold:
                    count += 1
                
                currAvg -= (arr[L] / k)
                L += 1

        return count