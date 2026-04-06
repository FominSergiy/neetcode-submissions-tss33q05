class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            going over the range and using nums[i] to modify
            array in-place, but duplicate checks we use actual
            array numbers and modify values based on nums adjusted
            for 0-index (nums - 1)
        '''

        # n = len(nums)
        # for i in range(n):
        #     num = abs(nums[i])
        #     # 0 -index -> need to decrement
        #     nums[num - 1] *= -1
        #     if nums[num - 1] > 0:
        #         return num

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        