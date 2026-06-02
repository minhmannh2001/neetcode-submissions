from typing import List


class Solution:
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:
            
            alive = True
            
            # Có khả năng va chạm
            while (
                alive
                and asteroid < 0
                and stack
                and stack[-1] > 0
            ):
                
                # Thiên thạch bên trái nhỏ hơn
                if stack[-1] < -asteroid:
                    stack.pop()
                
                # Hai thiên thạch bằng nhau
                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False
                
                # Thiên thạch hiện tại nhỏ hơn
                else:
                    alive = False
            
            if alive:
                stack.append(asteroid)
        
        return stack