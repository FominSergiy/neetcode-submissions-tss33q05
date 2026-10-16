class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # x XOR x = 0
        # 0 XOR y = y
        # x XOR x XOR y = y
        mask = 0
        for num in nums:
            mask ^= num
        return mask