class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        # our "window" is 2 pointers where left contracts as long as l > r
        # we contract, and calculate profit, profit init at 0
        profit = 0

        left = 0
        for right in range(1,len(prices)):
            while prices[left] > prices[right]:
                left += 1
            
            if left != right:
                profit = max(profit, prices[right] - prices[left])
        
        return profit

