class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1 for _ in range(len(s) + 1)]

        def backtrack(i):
            # đi hết chuỗi → 1 cách hợp lệ
            if i == n:
                return 1

            if memo[i] != -1:
                return memo[i]

            # bắt đầu bằng '0' → invalid
            if s[i] == '0':
                return 0

            # chọn 1 digit
            count = backtrack(i + 1)

            # chọn 2 digits nếu hợp lệ
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                count += backtrack(i + 2)

            memo[i] = count
            return count

        return backtrack(0)