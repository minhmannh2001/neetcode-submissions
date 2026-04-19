class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # B1: Count t
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        have = 0
        need_count = len(need)

        left = 0
        min_len = float("inf")
        result = ""

        # B2: Expand window
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Nếu ký tự này đủ số lượng như trong t
            if char in need and window[char] == need[char]:
                have += 1

            # Khi window đã hợp lệ → thu nhỏ
            while have == need_count:
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    result = s[left:right+1]

                # chuẩn bị thu nhỏ
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result
