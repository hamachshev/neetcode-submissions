class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix[0]) * len(matrix) -1

        while left <= right:
            mid = left + (right - left) // 2
            row, col = mid // len(matrix[0]), mid % len(matrix[0])
            curr = matrix[row][col]

            if curr < target:
                left = mid + 1
            elif curr > target:
                right = mid -1
            else:
                return True
        return False