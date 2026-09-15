class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        
        # it has to be a number evenly divisble by 2
        # otherwise there is no way to make 2 equal subsets
        if total % 2 != 0:
            return False
        
        half = total // 2

        # idea is, 2nd idx is any number before the half - since all stop at half
        # and we are really just building a half
        memo = [[-1] * (half + 1) for _ in range(n + 1)]
        # print(memo)
        def dp(i: int, cur_sum: int) -> bool:
            if cur_sum > half or i >= n:
                return False
            
            if cur_sum == half:
                return True
            
            # print(f"{i}, {cur_sum}")
            if memo[i][cur_sum] != -1:
                return memo[i][cur_sum]
            
            can = False
            for j in range(i, n):
                if cur_sum + nums[j] <= half:
                    can |= dp(j + 1, cur_sum + nums[j])
            
            memo[i][cur_sum] = can
            return memo[i][cur_sum]

        return dp(0, 0)
        