class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        frontIdx = 0
        backIdx = len(nums)

        while frontIdx < backIdx:
            if nums[frontIdx] == val:
                backIdx -= 1
                nums[frontIdx] = nums[backIdx]
            else:
                frontIdx += 1

        return frontIdx