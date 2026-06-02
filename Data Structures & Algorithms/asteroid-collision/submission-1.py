from typing import List


class Solution:
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        changed = True
        
        while changed:
            
            changed = False
            
            i = 0
            
            while i < len(asteroids) - 1:
                
                left = asteroids[i]
                right = asteroids[i + 1]
                
                # Có va chạm
                if left > 0 and right < 0:
                    
                    changed = True
                    
                    if abs(left) > abs(right):
                        
                        # Right explodes
                        asteroids.pop(i + 1)
                    
                    elif abs(left) < abs(right):
                        
                        # Left explodes
                        asteroids.pop(i)
                    
                    else:
                        
                        # Both explode
                        asteroids.pop(i + 1)
                        asteroids.pop(i)
                    
                    break
                
                i += 1
        
        return asteroids