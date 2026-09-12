class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # because negative numbers can negate
        # at each num we need to track cur_max, cur_min
        # an update each as we move along
        # keep track of either for tmp because result of previous max could be cur min if sign negates it
        res = nums[0]
        cur_max, cur_min = 1, 1
        for num in nums:
            tmp = cur_max * num
            cur_max = max(cur_max * num, cur_min * num, num)
            cur_min = min(tmp, cur_min * num, num)
            res = max(res, cur_max)
        return res
