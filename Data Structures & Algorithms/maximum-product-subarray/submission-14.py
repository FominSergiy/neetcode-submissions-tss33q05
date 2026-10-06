class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_cur, min_cur = 1, 1
        res = nums[0]

        for num in nums:
            tmp = max_cur * num
            max_cur = max(max_cur * num, min_cur * num, num)
            min_cur = min(tmp, min_cur * num, num)
            res = max(res, max_cur)
        
        return res