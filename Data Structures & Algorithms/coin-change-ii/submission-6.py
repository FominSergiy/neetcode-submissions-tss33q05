class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[None] * (amount + 1) for _ in range(len(coins) + 1)]

        def dp(i: int, amt: int) -> int:
            if amt == 0:
                return 1
            
            if i >= len(coins):
                return 0 # overshot
            
            if memo[i][amt] is not None:
                return memo[i][amt]
            
            # either take this coin or skip
            ways = 0
            if amt >= coins[i]:
                ways += dp(i + 1, amt)
                ways += dp(i, amt - coins[i]) # pick this coin and try again
            
            memo[i][amt] = ways
            return memo[i][amt]
        
        return dp(0, amount)

        # bottom up
        # n = len(coins)
        # coins.sort()
        # dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # for i in range(n + 1):
        #     dp[i][0] = 1
        
        # for i in range(n - 1, -1, -1):
        #     for a in range(amount + 1):
        #         if a >= coins[i]:
        #             dp[i][a] = dp[i + 1][a]
        #             dp[i][a] += dp[i][a - coins[i]]
        
        # return dp[0][amount]