class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        frontIdx = 0
        backIdx = len(nums) - 1

        while frontIdx <= backIdx:
            if nums[frontIdx] == val:
                
                nums[frontIdx] = nums[backIdx]
                backIdx -= 1
            else:
                frontIdx += 1

        return frontIdx