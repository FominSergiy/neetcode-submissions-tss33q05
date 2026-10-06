class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # use 2 pointers
        # for each position of i j we have following decisions
        # if chars are the same at idxs - move forward
        # if chars are different
        # take min of 3 operations
        # delete (i + 1, j)
        # isert: (i, j + 1)
        # replace (i + 1, j + 1)
        m, n = len(word1), len(word2)

        memo = {}
        def dp(i: int, j: int) -> int:
            # if reached end word 1 - add rem from word2 (n - j)
            if i == m:
                return n - j
            
            # if reached word2, add rem char from word1
            if j == n:
                return m - i
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
            else:
                # chars are different at i and j
                # delete, insert, skip
                res = min(dp(i + 1, j), dp(i, j + 1))
                res = min(res, dp(i + 1, j + 1))
                
                memo[(i, j)] = res + 1 # + 1 for current step change of 3 above
            return memo[(i, j)]
            
        return dp(0, 0)

            