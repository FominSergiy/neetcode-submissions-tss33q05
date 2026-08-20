class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(open_n: int, close_n: int):
            if open_n == 0 and close_n == 0:
                ans.append("".join(cur[:]))
                return
            
            if open_n > 0:
                cur.append("(")
                backtrack(open_n - 1, close_n)
                cur.pop()
            
            if close_n > open_n:
                cur.append(")")
                backtrack(open_n, close_n - 1)
                cur.pop()


        cur = []
        ans = []
        backtrack(n, n)
        return ans
        