from typing import List
import math


class SegmentTree:
    
    def __init__(self, size):
        self.n = size
        self.tree = [math.inf] * (4 * size)
    
    def update(self, node, start, end, left, right, value):
        
        # No overlap
        if right < start or end < left:
            return
        
        # Fully covered
        if left <= start and end <= right:
            self.tree[node] = min(self.tree[node], value)
            return
        
        mid = (start + end) // 2
        
        self.update(node * 2, start, mid, left, right, value)
        self.update(node * 2 + 1, mid + 1, end, left, right, value)
    
    def query(self, node, start, end, idx):
        
        if start == end:
            return self.tree[node]
        
        mid = (start + end) // 2
        
        current = self.tree[node]
        
        if idx <= mid:
            return min(current,
                       self.query(node * 2, start, mid, idx))
        else:
            return min(current,
                       self.query(node * 2 + 1, mid + 1, end, idx))


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        MAX_COORD = 10000
        
        seg = SegmentTree(MAX_COORD + 1)
        
        # Range Min Update
        for left, right in intervals:
            
            size = right - left + 1
            
            seg.update(
                1,
                0,
                MAX_COORD,
                left,
                right,
                size
            )
        
        res = []
        
        # Point Query
        for q in queries:
            
            ans = seg.query(
                1,
                0,
                MAX_COORD,
                q
            )
            
            if ans == math.inf:
                res.append(-1)
            else:
                res.append(ans)
        
        return res