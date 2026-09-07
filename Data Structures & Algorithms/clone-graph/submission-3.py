"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs traverse through the graph and make a map of old to new
        # if have in the map, return, otherwise build
        old_to_new = {}

        def dfs(root: 'Node'):
            if root in old_to_new:
                return old_to_new[root]
            

            new_node = Node(root.val)
            # since we use this to avoid inf loops, set this up before dfs
            # into neighbors
            old_to_new[root] = new_node
            for nei in root.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return old_to_new[root]
        
        # skip dfs into node if not defined
        return dfs(node) if node else None