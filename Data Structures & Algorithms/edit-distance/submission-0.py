class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i: int, j: int) -> int:
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = 1 + min(
                    dfs(i + 1, j),     # delete
                    dfs(i, j + 1),     # insert
                    dfs(i + 1, j + 1)  # replace
                )

            return memo[(i, j)]

        return dfs(0, 0)