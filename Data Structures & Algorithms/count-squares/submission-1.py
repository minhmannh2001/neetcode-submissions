from collections import defaultdict, Counter
from typing import List


class CountSquares:

    def __init__(self):
        
        # x -> Counter(y)
        self.columns = defaultdict(Counter)
        
        # Count every point
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        
        x, y = point
        
        self.columns[x][y] += 1
        
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        
        x1, y1 = point
        
        total = 0
        
        # Only iterate points in same column
        for y2, freq in self.columns[x1].items():
            
            # Same point not allowed
            if y1 == y2:
                continue
            
            d = abs(y2 - y1)
            
            # Right square
            total += (
                freq
                * self.points[(x1 + d, y1)]
                * self.points[(x1 + d, y2)]
            )
            
            # Left square
            total += (
                freq
                * self.points[(x1 - d, y1)]
                * self.points[(x1 - d, y2)]
            )
        
        return total