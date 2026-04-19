class Solution:
    def climbStairs(self, n: int) -> int:
        def mul(A, B):
            return [
                [A[0][0]*B[0][0] + A[0][1]*B[1][0],
                 A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0],
                 A[1][0]*B[0][1] + A[1][1]*B[1][1]]
            ]
        
        def power(M, n):
            res = [[1,0],[0,1]]
            while n:
                if n % 2:
                    res = mul(res, M)
                M = mul(M, M)
                n //= 2
            return res
        
        M = [[1,1],[1,0]]
        res = power(M, n-1)
        
        return res[0][0] + res[0][1]