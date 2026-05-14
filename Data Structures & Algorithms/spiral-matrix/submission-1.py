class Solution:
    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        left = 0
        right = cols - 1

        result = []

        while top <= bottom and left <= right:

            # 1. đi từ trái sang phải
            for c in range(left, right + 1):
                result.append(matrix[top][c])

            top += 1

            # 2. đi từ trên xuống dưới
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])

            right -= 1

            # 3. đi từ phải sang trái
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])

                bottom -= 1

            # 4. đi từ dưới lên trên
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])

                left += 1

        return result