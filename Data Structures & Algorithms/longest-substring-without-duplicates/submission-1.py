class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Nếu ký tự bên phải đã xuất hiện trong window
            # thì thu nhỏ window từ bên trái cho đến khi hết trùng
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Thêm ký tự mới vào window
            seen.add(s[right])

            # Cập nhật độ dài lớn nhất
            max_len = max(max_len, right - left + 1)

        return max_len
