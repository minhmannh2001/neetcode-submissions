class Solution:
    def maxArea(self, heights):
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            h = min(heights[l], heights[r])
            max_area = max(max_area, h * (r - l))

            if heights[l] < heights[r]:
                while l < r and heights[l] <= h:
                    l += 1
            else:
                while l < r and heights[r] <= h:
                    r -= 1

        return max_area
