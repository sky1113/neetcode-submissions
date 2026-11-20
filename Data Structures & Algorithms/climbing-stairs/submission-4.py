class Solution:
    def recurse(self, n, memo):
        if n in memo:
            return memo[n]
        n1 = self.recurse(n-1, memo)
        n2 = self.recurse(n-2, memo)
        memo[n] = n1 + n2
        return n1 + n2

    def climbStairs(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 2}
        if n in memo:
            return memo[n]

        return self.recurse(n-1, memo) + self.recurse(n-2, memo)