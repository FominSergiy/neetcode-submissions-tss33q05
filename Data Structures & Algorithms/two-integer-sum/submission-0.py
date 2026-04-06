class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if num in diff_map:
                j = diff_map[num]
                return sorted([i,j])
            
            diff_map[diff] = i
            