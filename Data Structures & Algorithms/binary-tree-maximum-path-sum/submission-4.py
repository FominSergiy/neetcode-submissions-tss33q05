# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            # grab vals from branches and discard any negative values
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # compute new max on this node taking both left and right
            max_sum = max(max_sum, node.val + left_max + right_max)

            # BUT - promote upward only 1 branch - max of left and right
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return max_sum
