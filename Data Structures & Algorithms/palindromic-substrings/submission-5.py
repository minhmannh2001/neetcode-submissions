class Solution:

    def countSubstrings(self, s: str) -> int:
        count = 0
        memo = [[0 for i in range(len(s))] for i in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 2:
                        memo[i][j] = 1
                        count+=1
                    else:
                        if memo[i+1][j-1] == 1:
                            memo[i][j] = 1
                            count+=1
            
        return count
        