from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        parent = list(range(n + 1))
        rank = [1] * (n + 1)  # size của mỗi tree
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX == rootY:
                return False  # cycle
            
            # union by rank (size)
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
                rank[rootX] += rank[rootY]
            else:
                parent[rootX] = rootY
                rank[rootY] += rank[rootX]
            
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]