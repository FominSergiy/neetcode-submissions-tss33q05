class Solution:
    def reverseBits(self, n: int) -> int:

        # get the bits first
        # reverse said bits
        bits = []

        for i in range(32):
            bit = 0
            if n & (1 << i):
                bit = 1
            bits.append(bit)

        res = 0
        for i, bit in enumerate(bits[::-1]):
            if bit == 1:
                res |= (1 << i)

        return res        