class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = top = 0
        right = len(matrix[0]) - 1
        down = len(matrix) - 1
        result = []
        while left <= right and top <= down:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            for row in range(top, down+1):
                result.append(matrix[row][right])
            right -= 1
            if top <= down:
                for col in reversed(range(left, right + 1)):
                    result.append(matrix[down][col])
                down -= 1
            if left <= right:
                for row in reversed(range(top, down + 1)):
                    result.append(matrix[row][left])
                left += 1
        return result
