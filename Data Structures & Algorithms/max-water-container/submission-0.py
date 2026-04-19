from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        left_index = 0
        right_index = 0

        # Duyệt tất cả các cặp (i, j) với i < j
        for i in range(n):
            for j in range(i + 1, n):
                width = j - i
                height = min(heights[i], heights[j])
                area = width * height

                if area > max_area:
                    max_area = area
                    left_index = i
                    right_index = j

        # Nếu cần debug / xem 2 cạnh nào tạo diện tích lớn nhất
        # print(f"Best container between indices {left_index} and {right_index}")

        return max_area