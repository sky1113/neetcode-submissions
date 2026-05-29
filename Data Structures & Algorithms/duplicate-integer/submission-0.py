class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr_idx = 0;
        curr_val = 0;
        while curr_idx < len(nums):
            curr_val = nums[curr_idx];
            for n in nums[curr_idx + 1 : len(nums)]:
                if n == curr_val:
                    return True;
            curr_idx += 1;
        return False;
         