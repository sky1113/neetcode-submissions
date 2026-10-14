class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        frontIdx = 0
        backIdx = len(nums) - 1

        while frontIdx < backIdx:
            print(frontIdx, backIdx)
            if nums[frontIdx] == val:
                if nums[backIdx] != val:
                    nums[frontIdx] = nums[backIdx]
                    nums[backIdx] = val
                backIdx -= 1
            else:
                frontIdx += 1
        
        if nums[frontIdx] != val:
            return frontIdx + 1
        else:
            return frontIdx