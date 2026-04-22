from collections import deque
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        maxLen = max(len(w) for w in wordDict)  # tối ưu
        
        n = len(s)
        queue = deque([0])   # bắt đầu từ index 0
        visited = set()      # tránh lặp
        
        while queue:
            start = queue.popleft()
            
            if start in visited:
                continue
            visited.add(start)
            
            # chỉ cần check trong phạm vi maxLen
            for end in range(start + 1, min(n + 1, start + maxLen + 1)):
                if s[start:end] in wordSet:
                    if end == n:
                        return True
                    queue.append(end)
        
        return False