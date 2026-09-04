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
