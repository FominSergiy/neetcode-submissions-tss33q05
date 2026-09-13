class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        if n == 1:
            return s in word_set
        
        # build top-down dp with start: int as starting idx, use 2 pointer to pattern match words from longer str
        memo = {}
        def dp(start: int) -> bool:
            if start == n:
                return True # reached the end
            
            if start in memo:
                return memo[start]
            can_split = False
            for end in range(start, n):
                word = s[start: end + 1]
                if word in word_set: # valid candidate - try this word
                    can_split |= dp(end + 1)
            
            memo[start] = can_split
            return memo[start]
        
        return dp(0)