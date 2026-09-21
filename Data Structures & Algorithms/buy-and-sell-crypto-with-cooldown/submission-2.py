class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        memo = {} # combine 2 values into a set! key = (idx, holding decision)
        def dp(i: int, holding: bool) -> int:
            if i >= n:
                return 0
            
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            # 3 opts
            # skip, sell or buy
            skip = dp(i + 1, holding) #< has to encode both - both when holding and not holding
            if holding:
                sell = dp(i + 2, False) + prices[i]
                # return max(skip, sell)
                memo[(i, holding)] = max(skip, sell)
            else:
                buy = dp(i + 1, True) - prices[i]
                # return max(skip, buy)
                memo[(i, holding)] = max(skip, buy)
            return memo[(i, holding)]
        
        return dp(0, False)