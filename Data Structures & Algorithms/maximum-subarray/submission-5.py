class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kaden's algorithm
        # if sum drops below 0 start again
        max_sum, cur_sum = float('-inf'), 0
        for num in nums:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)

            if cur_sum < 0:
                cur_sum = 0
        return max_sum

        # worth doing DP here as well - tmr?
        # simple choice - at each i we can either
        # start new subarray or extend the previous one
        # storing the max of either in the current i allows us to save
        # what is the longest subarray we can get at current index i
        # dp = nums[:]
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i - 1])
        # return max(dp)
