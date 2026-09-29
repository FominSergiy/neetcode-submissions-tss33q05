class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_cur, max_cur = 1, 1
        res = nums[0]

        # always have to have product of cur num and cur_max or cur_min
        for num in nums:
            tmp = max_cur * num
            max_cur = max(num * max_cur, num * min_cur, num)
            min_cur = min(tmp, num * min_cur, num)
            res = max(res, max_cur)
            # print(f"max: {max_cur}, min: {min_cur}")
        
        return res