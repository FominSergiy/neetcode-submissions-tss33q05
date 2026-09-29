class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = {}
        def dp(i: int, amt: int) -> int:
            if i == n:
                return 1 if amt == target else 0
            
            if (i, amt) in memo:
                return memo[(i, amt)]
            
            ways = dp(i + 1, amt - nums[i])
            ways += dp(i + 1, amt + nums[i])

            memo[(i, amt)] = ways
            return memo[(i, amt)]
        
        return dp(0, 0)