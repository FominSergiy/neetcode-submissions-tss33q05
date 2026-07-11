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
        
        # swap null values with -1001 later flip to none
        vals = []

        # explicitly set -1001 for None nodes
        # that way shape is known - each node has exactly 2 children
        def build_pre_order(node: Optional[TreeNode]) -> None:
            if not node:
                vals.append(-1001)
                return

            vals.append(node.val)
            build_pre_order(node.left)
            build_pre_order(node.right)
            return
        
        build_pre_order(root)
        return ",".join(map(str, vals))

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "[]":
            return None
        
        pre_str = [int(val) for val in data.split(",")]
        pre_order = []
        for val in pre_str:
            if val == -1001:
                pre_order.append(None)
            else:
                pre_order.append(val)
        
        def build(values: int | None):
            idx = 0
            # process a number at a time
            # children are known, exactly 2 nodes
            # processing in-order yields proper tree given global index
            def helper():
                nonlocal idx
                val = pre_order[idx]
                idx += 1
                if val is None:
                    return None

                node = TreeNode(val)
                node.left = helper()
                node.right = helper()
                return node
            return helper()

        return build(pre_order)

    

        
