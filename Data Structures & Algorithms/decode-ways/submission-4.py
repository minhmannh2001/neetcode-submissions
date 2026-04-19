class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        next1 = 1  # dp[i+1]
        next2 = 0  # dp[i+2]

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = next1
                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    curr += next2

            next2 = next1
            next1 = curr

        return next1