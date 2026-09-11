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
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # set a to be smallest of what it already is
                    # or what it could be if we take this coin and save
                    # result to a - c
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
        