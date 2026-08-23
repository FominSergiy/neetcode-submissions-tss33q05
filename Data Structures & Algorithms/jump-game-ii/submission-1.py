class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS-like solution over the array
        # use 2 pointers with l, r and update as we move along
        # always set r to r + 1
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, nums[i] + i)
            
            l = r + 1
            r = furthest
            res += 1
        
        return res