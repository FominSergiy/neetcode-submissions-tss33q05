class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dp(i: int, amt: int):
            if amt == 0:
                return 1
            
            if i >= len(coins):
                return 0
            
            if memo[i][amt] != -1:
                return memo[i][amt]
            

            res = 0
            if amt >= coins[i]:
                res = dp(i + 1, amt)
                res += dp(i, amt - coins[i])
            
            memo[i][amt] = res
            return memo[i][amt]
        
        return dp(0, amount)