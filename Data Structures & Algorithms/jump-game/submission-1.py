class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        # go backward from end
        # at each i we check against target
            # if we can reach target, we update target to be this i
                # this means we can reach target from this i
                # find earlist i that can reach this target
        
        # index we need to reach
        target = len(nums) - 1

        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= target:
                target = i

        return target == 0
        