class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]*len(nums)
        suffix = [nums[-1]]*len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1]*nums[i]
        
        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = suffix[j + 1]*nums[j]

        res = [0]*len(nums)
        res[0] = suffix[1]
        res[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            res[i] = prefix[i - 1] * suffix[i + 1]

        return res