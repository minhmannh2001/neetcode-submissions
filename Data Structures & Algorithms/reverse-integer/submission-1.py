class Solution:
    
    def reverse(self, x: int) -> int:
        
        MIN_INT = -(2 ** 31)
        MAX_INT = (2 ** 31) - 1
        
        sign = -1 if x < 0 else 1
        
        x = abs(x)
        
        result = 0
        
        while x > 0:
            
            digit = x % 10
            
            x //= 10
            
            # Check overflow before multiply
            if result > MAX_INT // 10:
                return 0
            
            # Edge case:
            if result == MAX_INT // 10 and digit > 7:
                return 0
            
            result = result * 10 + digit
        
        return result * sign