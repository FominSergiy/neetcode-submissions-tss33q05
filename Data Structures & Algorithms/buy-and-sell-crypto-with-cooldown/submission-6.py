class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        memo = {} # (i, holding) - 2 binary choices
         # 3 choises - skip, buy or sell
        def dp(i: int, holding: bool) -> int:
            if i >= n:
                return 0
            
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            
            skip = dp(i + 1, holding)
            if holding:
                sell = dp(i + 2, False) + prices[i]
                memo[(i, holding)] = max(sell, skip)
            else:
                buy = dp(i + 1, True) - prices[i]
                memo[(i, holding)] = max(buy, skip)
            
            return memo[(i, holding)]
        
        return dp(0, False)
        
