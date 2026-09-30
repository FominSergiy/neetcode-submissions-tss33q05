class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_cur, max_cur = 1, 1
        res = nums[0]

        for num in nums:
            tmp = num * max_cur
            max_cur = max(max_cur * num, min_cur * num, num)
            min_cur = min(tmp, min_cur * num, num)
            res = max(max_cur, res)
        
        return res