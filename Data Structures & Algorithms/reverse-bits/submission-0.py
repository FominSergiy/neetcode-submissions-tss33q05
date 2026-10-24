class Solution:
    def reverseBits(self, n: int) -> int:

        # get the bits first
        # reverse said bits
        bits = []

        for i in range(32):
            bit = 0
            # 1 & 1 gives 1, 1 & 0 gets us zero
            if n & (1 << i): # check bit at possition i with mask
                bit = 1
            bits.append(bit)
        
        # now work in reversed order, use or operator to set bits
        # in number
        res = 0
        for i, bit in enumerate(bits[::-1]):
            if bit == 1:
                res |= (1 << i) # set only the i-th bit # or leaves rest untouched
        
        return res

        