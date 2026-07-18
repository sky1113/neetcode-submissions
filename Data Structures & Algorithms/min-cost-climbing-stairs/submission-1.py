class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])

        dp = [0] * (n + 1)
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # top floor, since we have to go past the last index of cost
        dp[n] = min(dp[n - 1], dp[n - 2])
        return dp[n]
