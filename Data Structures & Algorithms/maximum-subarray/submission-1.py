class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kaden's - greedy
        # if sum drops below 0 start again
        max_sub, cur_sum = nums[0], 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num
            max_sub = max(max_sub, cur_sum)
        
        return max_sub