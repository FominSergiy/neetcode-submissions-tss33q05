class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # maintain individual counts for each char
        # only add ( when ) > (
        def backtrack(count_o: int, count_c: int):
            if count_o == 0 and count_c == 0:
                ans.append("".join(cur[:]))
                return
            
            #1. if we ahve open, put open - backtrack
            if count_o > 0:
                cur.append("(")
                backtrack(count_o - 1, count_c)
                cur.pop()

            #1. otherwise if closed > open - backtrack
            if count_c and count_c > count_o:
                cur.append(")")
                backtrack(count_o, count_c - 1)
                cur.pop()


        cur = []
        ans = []
        backtrack(n, n)
        return ans
        