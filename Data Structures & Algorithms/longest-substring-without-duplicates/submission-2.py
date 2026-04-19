class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0

        for right, c in enumerate(s):
            # Nếu ký tự đã xuất hiện và vẫn nằm trong window hiện tại
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1

            # Cập nhật vị trí xuất hiện gần nhất của ký tự
            last_seen[c] = right

            # Cập nhật độ dài lớn nhất
            max_len = max(max_len, right - left + 1)

        return max_len
