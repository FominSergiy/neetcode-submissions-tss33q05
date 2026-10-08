class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # skip if match
        # otherwise take the min of 3 actions
        # delete
        # insert
        # replace
        m, n = len(word1), len(word2)
        memo = {}

        def dp(i: int, j: int) -> int:
            if i == m:
                return n - j
            
            if j == n:
                return m - i
            
            if (i, j) in memo:
                return memo[(i, j)]
            

            if word1[i] == word2[j]:
                memo[(i, j)] =dp(i + 1, j + 1)
            else:
                res = min(dp(i + 1, j), dp(i, j + 1))
                res = min(res, dp(i + 1, j + 1))
                memo[(i, j)] = res + 1
            return memo[(i, j)]
        
        return dp(0, 0)