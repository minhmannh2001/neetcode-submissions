class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        n = len(s)

        # Try all start positions
        for start in range(n):
            # Try all end positions
            for end in range(start, n):
                # Check if substring [start, end] can be made uniform
                if self.can_make_uniform(s, start, end, k):
                    max_len = max(max_len, end - start + 1)

        return max_len

    def can_make_uniform(self, s: str, start: int, end: int, k: int) -> bool:
        # Try every uppercase letter as target
        for target in range(ord('A'), ord('Z') + 1):
            count_diff = 0

            for i in range(start, end + 1):
                if s[i] != chr(target):
                    count_diff += 1

            if count_diff <= k:
                return True

        return False
