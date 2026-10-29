class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # O(n) -> too slow
        # res = 1
        # for _ in range(abs(n)):
        #     res *= x
        
        # return res if n >= 0 else 1 / res

        # do log iteration with halving each time
        # O(logn)
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        factor = abs(n)
        while factor:
            # if odd multiply 1 more time
            if factor % 2 != 0:
                res *= x
            x *= x
            factor //= 2
        return res if n >= 0 else 1 / res

