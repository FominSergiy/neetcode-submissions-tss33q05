class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kaden's algorithm
        # if sum drops below 0 start again
        cur_sum, max_sum = 0, float('-inf')
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
        return max_sum


        # worth doing DP here as well - tmr?