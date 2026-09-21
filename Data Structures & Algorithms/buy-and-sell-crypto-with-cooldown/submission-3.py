class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # # TOP DOWN
        # n = len(prices)
        # memo = {} # combine 2 values into a set! key = (idx, holding decision)
        # def dp(i: int, holding: bool) -> int:
        #     if i >= n:
        #         return 0
            
        #     if (i, holding) in memo:
        #         return memo[(i, holding)]
            
        #     # 3 opts
        #     # skip, sell or buy
        #     skip = dp(i + 1, holding) #< has to encode both - both when holding and not holding
        #     if holding: 
        #         sell = dp(i + 2, False) + prices[i]
        #         memo[(i, holding)] = max(skip, sell)
        #     else:
        #         buy = dp(i + 1, True) - prices[i]
        #         memo[(i, holding)] = max(skip, buy)
        #     return memo[(i, holding)]
        
        # return dp(0, False)

        # BOTTOM UP
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for holding in [True, False]:
                if holding:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    skip = dp[i + 1][False] if i < n else 0
                    dp[i][0] = max(sell, skip)
                else:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    skip = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, skip)

        
        return dp[0][1]
