class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (n * m) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # to get col, mid % m - 1 -> this gives us row number belongs to
            # for position in row, we grab mid - row % n - 1 -> this gives us position in row
            row = mid // n
            col = mid % n

            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                return True
        return False