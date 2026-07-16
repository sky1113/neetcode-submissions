class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        memo = [0] * (n + 1)
        memo[1], memo[2] = 1, 2
        
        for k in range(3, n + 1):
            memo[k] = memo[k - 2] + memo[k - 1]
        
        return memo[n]