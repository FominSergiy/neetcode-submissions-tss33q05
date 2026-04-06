class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float("-inf")

        left = 0
        right = len(heights) - 1

        while left < right:
            # computer current area
            min_height = min(heights[left], heights[right])
            
            distance = right - left
            max_area = max(max_area, distance * min_height)

            # move pointers
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area