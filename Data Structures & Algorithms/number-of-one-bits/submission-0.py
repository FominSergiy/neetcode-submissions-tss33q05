class Solution:
    def hammingWeight(self, n: int) -> int:
        # res = 0
        # while n:
        #     res += n % 2 # get last bit 1 % 2 -> 1 and 0 % 2 -> 0
        #     n = n >> 1 # shift bits to right and try next bit on right
        # return res

        # special
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res