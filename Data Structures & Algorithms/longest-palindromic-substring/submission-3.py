class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            while i >= 0 and j <= len(s)-1 and s[i] == s[j]:
                i-=1
                j+=1
            return i+1, j-1
        
        start = 0
        end = 0

        for i in range(len(s)):
            i1, j1 = expand(i, i)
            if j1 - i1 > end - start:
                start = i1
                end = j1
        
        for i in range(len(s)):
            i2, j2 = expand(i, i + 1)
            if j2 - i2 > end - start:
                start = i2
                end = j2
        
        return s[start:end+1]


        