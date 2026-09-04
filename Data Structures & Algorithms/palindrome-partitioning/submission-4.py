class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []

        def is_pali(l: int, r: int, word: str) -> bool:
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True


        def backtrack(i: int):
            if i >= len(s):
                ans.append(part[:])
                return
            
            # main iteration
            for j in range(i, len(s)):
                if is_pali(i, j, s): # pass the actual word, we have indicies, rest does not matter
                    part.append(s[i: j + 1]) # right bound is excluse hense + 1 to include j
                    backtrack(j + 1)
                    part.pop()
        



        backtrack(0)
        return ans
