# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # pass boudaries down

        def is_bst(node: TreeNode, l_bound: float, r_bound: float) -> bool:
            if not node:
                return True
            
            left = is_bst(node.left, l_bound, node.val)
            right = is_bst(node.right, node.val, r_bound)

            return l_bound < node.val < r_bound and left and right
        


        return is_bst(root, float("-inf"), float("inf"))
