class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        memo = [[-1] * 2 for _ in range(len(nums))]
        # perform 2 dp - 1 n
        def dp(i: int, flag: bool):
            if i == 0 and flag:
                return nums[0]
            elif i <= 0:
                return 0
            
            if memo[i][flag] != -1:
                return memo[i][flag]
            
            memo[i][flag] = max(dp(i - 1, flag), dp(i - 2, flag) + nums[i])
            return memo[i][flag]
        
        return max(dp(n - 1, False), dp(n - 2, True))
            
            

