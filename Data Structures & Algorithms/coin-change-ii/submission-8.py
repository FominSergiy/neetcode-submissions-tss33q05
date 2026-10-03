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
            
            ways = dp(i + 1, amt)
            if amt >= coins[i]:
                ways += dp(i, amt - coins[i])
            
            memo[i][amt] = ways
            return memo[i][amt]
        
        return dp(0, amount)

