class Solution:
    def checkValidString(self, s: str) -> bool:
        # use 2 stacks, for left and for the star
        # keep idx inside the stack
        # at the end, any unmatched open parenthesis - check against idx of stars
        left_stack = []
        star_stack = []

        for i in range(len(s)):
            char = s[i]
            if char == "(":
                left_stack.append(i)
            elif char == "*":
                star_stack.append(i)
            else:
                if not left_stack and not star_stack:
                    return False
                elif left_stack:
                    left_stack.pop()
                else:
                    star_stack.pop()
        

        # match unclosed (
        while left_stack and star_stack:
            if left_stack.pop() > star_stack.pop():
                return False
        
        # might have exhausted stars but kept some brackets open
        return True if not left_stack else False