class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS-like solution over the array
        # it is a graph search over a flat array
        # we start by taking 1 more jump and find what is the furthest we can jump to
        # that becomes our right bound, our left bound is previous r + 1
        # + 1 because we already explored previous options
        l, r = 0, 0
        jumps = 0
        while r < len(nums) - 1:
            furthest = r
            for i in range(l, r + 1): # 1 more jump
                furthest = max(nums[i] + i, furthest) # add position + how far we can jump from a given position
            
            l = r + 1
            r = furthest
            jumps += 1
        return jumps
    