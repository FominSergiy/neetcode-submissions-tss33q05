class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(i: int):
            if i >= len(s):
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                if self.is_pali(s, i, j):
                    part.append(s[i: j + 1])
                    backtrack(j + 1)
                    part.pop()
        
        backtrack(0)
        return res
    
    def is_pali(self, s: str, l: int, r: int) -> bool:
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True