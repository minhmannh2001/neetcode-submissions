from collections import Counter
from typing import List


class CountSquares:

    def __init__(self):
        
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        
        x, y = point
        
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        
        qx, qy = point
        
        res = 0
        
        for (x, y), freq in self.points.items():
            
            # Must form diagonal
            if abs(x - qx) != abs(y - qy):
                continue
            
            # Side length cannot be zero
            if x == qx:
                continue
            
            # Other two corners
            point1 = (x, qy)
            point2 = (qx, y)
            
            res += (
                freq
                * self.points[point1]
                * self.points[point2]
            )
        
        return res