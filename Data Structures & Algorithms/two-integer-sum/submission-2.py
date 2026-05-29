class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set(nums)
        for i in range(len(nums)):
            curr_compliment = target - nums[i]
            if curr_compliment in num_set:
                if nums[i] == curr_compliment and nums.count(nums[i]) == 1:
                    continue 
                return [i, nums.index(curr_compliment, i + 1)]
            continue