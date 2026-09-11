class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def dp(amt: int):
            if amt == 0:
                return 0
            
            if amt in memo:
                return memo[amt]
            
            res = float('inf')
            for coin in coins[::-1]:
                if amt - coin >= 0:
                    res = min(res, 1 + dp(amt - coin))

            memo[amt] = res
            return memo[amt]
        

        ans = dp(amount)
        return ans if ans != float('inf') else -1
        