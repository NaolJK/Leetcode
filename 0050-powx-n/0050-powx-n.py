class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow_c(x,n):
            if n == 0:
                return 1
            mid = pow_c(x, n//2)

            if n % 2 == 0:
                return mid * mid
            else:
                return mid * mid * x

        if n < 0:
            x = 1/x
            return pow_c(x,-n)
        return pow_c(x,n)
