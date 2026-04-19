class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        n = len(s)

        # Try all start positions
        for start in range(n):
            count = [0] * 26   # frequency of A-Z
            max_count = 0     # highest frequency in current window

            # Expand the end pointer
            for end in range(start, n):
                # Add current character
                index = ord(s[end]) - ord('A')
                count[index] += 1

                # Update max frequency in this window
                max_count = max(max_count, count[index])

                length = end - start + 1
                need_change = length - max_count

                # If valid
                if need_change <= k:
                    max_len = max(max_len, length)

        return max_len
