# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # construct map from in-order to get idx fast
        in_order_map = { val: idx for idx, val in enumerate(inorder)}

        root_val = preorder[0]
        mid = in_order_map[root_val]

        n = len(preorder)

        # offset since we took 1st elem as root
        left = self.buildTree(preorder[1: mid + 1], inorder[0: mid])
        right = self.buildTree(preorder[mid + 1: n], inorder[mid + 1: n])

        node = TreeNode(root_val, left=left, right=right)
        return node



            

        