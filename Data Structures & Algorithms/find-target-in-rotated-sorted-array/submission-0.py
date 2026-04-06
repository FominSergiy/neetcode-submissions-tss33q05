class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot - smallest point in arr
        n = len(nums)

        l = 0
        r = n - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[r]: # smallest in [left:mid]
                r = mid
            else:
                l = mid + 1 #in right (mid:right]
        
        # define new search space / or return if pivot is target
        pivot = l

        l = 0
        r = n - 1

        # using right segment as a gauge
        # if target is greater than the biggest num in right segment
        # it has to be in the left segment
        right_segment = nums[pivot:]

        if target > right_segment[-1]:
            r = pivot -1
        else:
            l = pivot


        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1