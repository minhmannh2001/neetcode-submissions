from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            h = heights[i]

            left = i
            while left >= 0 and heights[left] >= h:
                left -= 1

            right = i
            while right < n and heights[right] >= h:
                right += 1

            width = right - left - 1
            area = h * width

            max_area = max(max_area, area)

        return max_area