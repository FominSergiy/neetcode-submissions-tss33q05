class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min, cur_max = 1, 1

        for num in nums:
            tmp = cur_max * num
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(tmp, num * cur_min, num)
            res = max(res, cur_max)
        
        return res