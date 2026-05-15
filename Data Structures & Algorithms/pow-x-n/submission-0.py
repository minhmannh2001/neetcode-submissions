class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # x^0 = 1
        if n == 0:
            return 1
        
        # Handle negative power
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        
        # Multiply x, n times
        for _ in range(n):
            result *= x
        
        return result