class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        res = [-1] * n
        res[-1] = 1
        res[-2] = 2

        for i in range(len(res)-3, -1, -1):
            res[i] = res[i+1] + res[i+2]
        return res[0]