class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = [0] * (len(nums) + 1)

        self.pre[1] = nums[0]

        for i in range(1, len(nums)):
            self.pre[i + 1] = self.pre[i] + nums[i]
        
        print(self.pre)
            

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)