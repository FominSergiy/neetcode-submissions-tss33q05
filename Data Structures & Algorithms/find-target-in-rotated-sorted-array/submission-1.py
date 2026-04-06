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

        # or alternatively, search both spaces
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        # do binary search on left half
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        
        # if negative -1 -> try looking at right half first
        return binary_search(pivot, n - 1)
        