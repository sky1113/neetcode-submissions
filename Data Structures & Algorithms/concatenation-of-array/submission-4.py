class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * (length * 2)
        for i, num in enumerate(nums):
            ans[i] = ans[length + i] = num

        return ans