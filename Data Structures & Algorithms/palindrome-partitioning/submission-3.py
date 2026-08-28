class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []

        # at each index i we have either a valid paindrom or not
        # if its valid, we add it part and recurse
        # if not, we try next idx
        def backtrack(i: int):
            if i >= len(s):
                ans.append(part[:])
                return
            
            for j in range(i, len(s)):
                if self.is_pali(s, i, j):
                    part.append(s[i: j + 1])
                    backtrack(j + 1)
                    part.pop()
        
        backtrack(0)
        return ans

    
    def is_pali(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
