class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # XORR
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr
        