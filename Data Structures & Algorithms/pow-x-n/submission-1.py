class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        
        # Handle negative power
        if n < 0:
            x = 1 / x
            n = -n
        
        def power(x, n):
            
            # Base case
            if n == 0:
                return 1
            
            half = power(x, n // 2)
            
            # Even exponent
            if n % 2 == 0:
                return half * half
            
            # Odd exponent
            return x * half * half
        
        return power(x, n)