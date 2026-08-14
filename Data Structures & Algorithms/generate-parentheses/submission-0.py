class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # maintain individual counts for each char
        # only add ( when ) > (
        def backtrack(count_o: int, count_c: int):
            if count_o == 0 and count_c == 0:
                ans.append("".join(cur[:]))
                return
            
            # by default go with open (bracket needs l for r = () )
            if count_o > 0:
                cur.append("(")
                backtrack(count_o - 1, count_c)
                cur.pop()

            # keep closing as long as closed > open
            if count_c > count_o:
                cur.append(")")
                backtrack(count_o, count_c - 1)
                cur.pop()


        cur = []
        ans = []
        backtrack(n, n)
        return ans
        