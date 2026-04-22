class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        lengths = set(len(w) for w in wordDict)
        
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for l in lengths:
                if i - l >= 0 and dp[i - l] and s[i - l:i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[n]