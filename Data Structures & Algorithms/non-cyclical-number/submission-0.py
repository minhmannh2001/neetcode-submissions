class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n != 1:
            
            # Cycle detected
            if n in seen:
                return False
            
            seen.add(n)
            
            new_num = 0
            
            # Sum of square of digits
            while n > 0:
                
                digit = n % 10
                
                new_num += digit * digit
                
                n //= 10
            
            n = new_num
        
        return True