class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(i, j):
            # base case: hết 1 trong 2 string → không còn ký tự để so
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            # nếu 2 ký tự hiện tại match → tiến cả 2 con trỏ, cộng 1
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            # không match → thử 2 hướng, lấy max
            else:
                memo[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))

            return memo[(i, j)]
        
        return dfs(0, 0)