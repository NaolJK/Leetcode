class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = - n
        if x == 0:
            return 0
        if x == 1:
            return 1
        if n == 0:
            return 1
        def pow_c(x,n):
            if n == 1:
                return x
            mid = pow_c(x, n//2)

            if n % 2 == 0:
                return mid * mid
            else:
                return mid * mid * x
            
        return pow_c(x,n)