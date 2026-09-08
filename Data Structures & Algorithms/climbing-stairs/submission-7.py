class Solution:
    def climbStairs(self, n: int) -> int:
        # fib sequence
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        
        # return dp[n]

        memo = {}
        # dfs dp
        def dp(i: int):
            if i == 0 or i == 1:
                return 1
            
            if i in memo:
                return memo[i]
            memo[i] =  dp(i - 1) + dp (i - 2)
            return memo[i]
        
        return dp(n)


