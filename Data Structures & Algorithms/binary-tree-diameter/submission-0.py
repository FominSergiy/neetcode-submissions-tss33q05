# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_step = 0
        def dfs(node: Optional[TreeNode]):
            nonlocal max_step
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            max_step = max(max_step, left + right)
            return max(left, right) + 1
        
        dfs(root)
        return max_step


