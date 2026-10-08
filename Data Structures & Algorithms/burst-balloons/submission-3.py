class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # if we think about using l r and define the boundaries
        # and that we burst the LAST balloon in l ,r
        # the boudaries become l - 1, r + 1, since range of [l,r] is empty
        # dont forget the padding
        memo = {}

        nums = [1] + nums + [1]
        def dp(l: int, r: int) -> int:
            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            max_coin = float('-inf')
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dp(l, i - 1) + dp(i + 1, r)
                max_coin = max(max_coin, coins)
            
            memo[(l, r)] = max_coin
            return memo[(l, r)]
                

        return dp(1, len(nums) - 2)
                