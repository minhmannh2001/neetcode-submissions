class Solution:
    def maxArea(self, heights):
        left = 0
        right = len(heights) - 1

        max_area = 0
        best_l = 0
        best_r = 0

        while left < right:
            width = right - left
            h = min(heights[left], heights[right])
            area = width * h

            if area > max_area:
                max_area = area
                best_l = left
                best_r = right

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
