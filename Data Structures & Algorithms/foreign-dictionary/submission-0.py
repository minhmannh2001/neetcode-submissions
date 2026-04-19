from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # tập hợp tất cả ký tự xuất hiện
        chars = set(''.join(words))

        # build graph từ các cặp từ liền kề
        adj = defaultdict(set)   # c1 → set of c2 (c1 < c2)
        in_degree = {c: 0 for c in chars}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            # prefix check: "abc" trước "ab" → invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break   # chỉ lấy ký tự KHÁC ĐẦU TIÊN

        # Topological Sort — BFS (Kahn's algorithm)
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        result = []

        while queue:
            c = queue.popleft()
            result.append(c)

            for neighbor in adj[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # nếu result không chứa hết tất cả ký tự → có cycle → invalid
        if len(result) != len(chars):
            return ""

        return ''.join(result)