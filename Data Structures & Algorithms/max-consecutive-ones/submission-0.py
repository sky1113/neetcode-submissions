class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSum = 0
        currSum = 0

        for n in nums:
            if n == 0:
                maxSum = max(maxSum, currSum)
                currSum = 0
            if n == 1:
                currSum += 1
            
        maxSum = max(maxSum, currSum)
        return maxSum

