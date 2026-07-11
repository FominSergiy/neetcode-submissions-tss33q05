# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "[]"

        pre_order = []
        in_order = []

        def build_pre_order(node: Optional[TreeNode]):
            if not node:
                return
            
            pre_order.append(node.val)
            build_pre_order(node.left)
            build_pre_order(node.right)
            return
        
        def build_in_order(node: Optional[TreeNode]):
            if not node:
                return
            
            build_in_order(node.left)
            in_order.append(node.val)
            build_in_order(node.right)
            return
        
        build_pre_order(root)
        build_in_order(root)
        
        # delim each value with ,
        pre_str = ",".join(map(str, pre_order))
        in_str = ",".join(map(str, in_order))

        # delim 2 lists with |
        return pre_str + "|" + in_str

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "[]":
            return None
    
        pre_str, in_str = data.split("|")
        pre_order = [int(val) for val in pre_str.split(",")]
        in_order = [int(val) for val in in_str.split(",")]

        in_order_map = { val: idx for idx, val in enumerate(in_order)}

        def _build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
            in_order_map = { val: idx for idx, val in enumerate(inorder)}
            
            if not preorder or not inorder:
                return None
            
            node_val = preorder[0]
            mid_idx = in_order_map[node_val]

            left = _build_tree(preorder[1: mid_idx + 1], inorder[0: mid_idx])
            right = _build_tree(preorder[mid_idx + 1:], inorder[mid_idx + 1:])

            node = TreeNode(val=node_val, left=left, right=right)
            return node

        tree = _build_tree(pre_order, in_order)
        return tree    

        
