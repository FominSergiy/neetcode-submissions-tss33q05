# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # keep is_balanced, depth as an item returned in dfs
        # check for bools and difference - return the result
        # [bool, depth]
        def dfs(node: Optional[TreeNode]):
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            is_bal = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            if not is_bal:
                return [False, 0]
            else:
                return [True, max(left[1], right[1]) + 1]

        
        return dfs(root)[0]

        