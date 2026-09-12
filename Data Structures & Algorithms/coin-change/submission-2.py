class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # TOP-DOWN
        # memo = {}
        # def dp(amt: int):
        #     if amt == 0:
        #         return 0
            
        #     if amt in memo:
        #         return memo[amt]
            
        #     res = float('inf')
        #     for coin in coins[::-1]:
        #         if amt - coin >= 0:
        #             res = min(res, 1 + dp(amt - coin))

        #     memo[amt] = res
        #     return memo[amt]
        

        # ans = dp(amount)
        # return ans if ans != float('inf') else -1

        #BOTTOM-UP
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # we reached starting point
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1) # min of current amount or taking current coin and adding one
        
        return dp[amount] if dp[amount] != amount + 1 else -1
        