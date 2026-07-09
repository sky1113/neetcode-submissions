class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0

        while low <= high:
            mid = low + ((high - low) // 2)
            print(nums[mid])
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
        
        return -1