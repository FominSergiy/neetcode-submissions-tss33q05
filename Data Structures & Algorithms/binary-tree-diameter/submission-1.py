# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # since it can be a max that does not go through the root we need
        # at each root check if that is the max
        # return back max of left or right
        max_length = 0
        def dfs(node: Optional[TreeNode]):
            nonlocal max_length
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            max_length = max(max_length, left + right)
            return max(left, right) + 1

        dfs(root)
        return max_length


