class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        memo = [[None] * (amount + 1) for _ in range(n + 1)]

        def dp(i: int, amt: int) -> int:
            if amt == 0:
                return 1
            
            if i >= n:
                return 0 # overshot
            
            if memo[i][amt] is not None:
                return memo[i][amt]
            

            # 2 choices - try this coin, or skip and try next one
            ways = 0
            if amt >= coins[i]:
                ways += dp(i + 1, amt) # skip
                ways += dp(i, amt - coins[i]) # try this coin
            
            memo[i][amt] = ways
            return memo[i][amt]
        
        return dp(0, amount)
