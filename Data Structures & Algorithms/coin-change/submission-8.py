class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # TOP-DOWN
        # memo = {}
        # def dp(amt: int) -> int:
        #     if amt == 0:
        #         return 0
            
        #     if amt in memo:
        #         return memo[amt]
            
        #     need = float('inf')
        #     for c in coins:
        #         if amt - c >= 0:
        #             need = min(need, 1 + dp(amt - c))
            
        #     memo[amt] = need
        #     return memo[amt]
        
        # ans = dp(amount)
        # return ans if ans != float('inf') else -1

        #BOTTOM-UP
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # iterating over the amount what I am saying is
        # at any amount a is there a coin where a - c >= 0
        # if such coin exists, then dp[a] = min(already existing value dp[a])
        # or value of dp[a - c] + 1 -> value of dp at that amount + 1 for using the coin
        for a in range(amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
