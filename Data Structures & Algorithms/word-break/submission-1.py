class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        maxLen = max(len(w) for w in wordDict)
        
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # base case
        
        for i in range(1, n + 1):
            # chỉ cần check các độ dài có thể
            for l in range(1, maxLen + 1):
                if i - l < 0:
                    break
                
                # nếu prefix trước đó hợp lệ + substring hiện tại nằm trong dict
                if dp[i - l] and s[i - l:i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[n]