class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_count = 0      # highest frequency in current window
        max_len = 0
        left = 0

        for right in range(len(s)):
            # Add right character to window
            index = ord(s[right]) - ord('A')
            count[index] += 1

            # Update max frequency
            max_count = max(max_count, count[index])

            # Current window length
            window_len = right - left + 1

            # If invalid → shrink from left
            if window_len - max_count > k:
                left_index = ord(s[left]) - ord('A')
                count[left_index] -= 1
                left += 1

            # Update result
            max_len = max(max_len, right - left + 1)

        return max_len
