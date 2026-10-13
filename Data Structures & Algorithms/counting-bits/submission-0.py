class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 -> 7
        # 0000 0 
        # 0001 1
        # 0010 2
        # 0011 3
        # 0100 4
        # 0101 5
        # 0110 6
        # 0111 7
        # 1000 8
        # we only move the offset once offset * 2 == i
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
        