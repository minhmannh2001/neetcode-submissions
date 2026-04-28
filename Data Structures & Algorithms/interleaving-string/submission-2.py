class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # luôn để s2 là chuỗi ngắn hơn để tối ưu space
        if len(s2) > len(s1):
            s1, s2 = s2, s1

        m, n = len(s1), len(s2)
        dp = [False] * (n + 1)

        dp[0] = True

        # init hàng đầu tiên (chỉ dùng s2)
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # cập nhật cột đầu (chỉ dùng s1)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                k = i + j
                dp[j] = (dp[j] and s1[i - 1] == s3[k - 1]) or \
                        (dp[j - 1] and s2[j - 1] == s3[k - 1])

        return dp[n]