class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0

        left_max = float('-inf')
        right_max = float('-inf')

        left = 0
        right = len(height) - 1

        while left < right:
            left_val = height[left]
            right_val = height[right]

            # check current pointers against new max
            left_max = max(left_val, left_max)
            right_max = max(right_val, right_max)

            # update area by taking max - current pointer values
            area += left_max - left_val
            area += right_max - right_val

            # decide which pointer to move
            if left_val <= right_val:
                left += 1
            else:
                right -= 1
        
        return area


        