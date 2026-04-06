class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            # 0 -index -> need to decrement
            nums[num - 1] *= -1
            if nums[num - 1] > 0:
                return num

        