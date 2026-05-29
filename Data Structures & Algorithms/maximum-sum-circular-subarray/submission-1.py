class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMin, globMax = nums[0], nums[0]
        currMin, currMax = nums[0], nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            currMax = max(nums[i], nums[i] + currMax)
            currMin = min(nums[i], nums[i] + currMin)

            globMax = max(currMax, globMax)
            globMin = min(currMin, globMin)

            total += nums[i]

        if total == globMin:
            return globMax
        else:
            return max(globMax, total - globMin)
