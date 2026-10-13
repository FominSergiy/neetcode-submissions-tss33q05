class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 0 # XOR on even is 1
        for num in nums:
            mask ^= num
        return mask
        