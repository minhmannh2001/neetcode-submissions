from collections import defaultdict

class Solution:
    def foreignDictionary(self, words):
        adj = defaultdict(set)
        
        # build graph (y như bạn)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}  # 0,1,2
        res = []
        
        def dfs(c):
            if c in visited:
                return visited[c] == 2
            
            visited[c] = 1  # visiting
            
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            
            visited[c] = 2
            res.append(c)
            return True
        
        for c in set(''.join(words)):
            if not dfs(c):
                return ""
        
        return ''.join(res[::-1])