from collections import Counter
from typing import List


class CountSquares:

    def __init__(self):
        
        # Count frequency of each point
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        
        x, y = point
        
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        
        x1, y1 = point
        
        total = 0
        
        # Try every point as vertical partner
        for (x2, y2), freq in self.points.items():
            
            # Must be on same vertical line
            if x1 != x2:
                continue
            
            # Cannot be same point
            if y1 == y2:
                continue
            
            # Side length of square
            d = abs(y2 - y1)
            
            # Square to the right
            total += (
                freq
                * self.points[(x1 + d, y1)]
                * self.points[(x1 + d, y2)]
            )
            
            # Square to the left
            total += (
                freq
                * self.points[(x1 - d, y1)]
                * self.points[(x1 - d, y2)]
            )
        
        return total