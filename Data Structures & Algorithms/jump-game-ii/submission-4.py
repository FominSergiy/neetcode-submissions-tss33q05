class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS-like solution over the array
        # it is a graph search over a flat array
        # we start by taking 1 more jump and find what is the furthest we can jump to
        # that becomes our right bound, our left bound is previous r + 1
        # + 1 because we already explored previous options
        l, r = 0, 0
        count = 0
        while r < len(nums) - 1:
            furthest = r
            for i in range(l, r + 1): # 1 more jump:
                furthest = max(furthest, nums[i] + i) # record actual jump
            
            l = r + 1
            r = furthest
            count += 1
        return count
