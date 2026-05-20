class Solution:
    
    def reverse(self, x: int) -> int:
        
        MIN_INT = -(1 << 31)
        MAX_INT = (1 << 31) - 1
        
        sign = -1 if x < 0 else 1
        
        x = abs(x)
        
        result = 0
        
        while x:
            
            digit = x % 10
            
            x //= 10
            
            # result * 10 using shifts
            new_result = (result << 3) + (result << 1) + digit
            
            if new_result > MAX_INT:
                return 0
            
            result = new_result
        
        return result * sign