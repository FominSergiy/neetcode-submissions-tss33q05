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

        def dfs(node: Optional['Node']):
            if node in old_to_new:
                return old_to_new[node]
            
            # create mapping old to new BEFORE dfs into
            # otherwise endless loop
            new_node = Node(node.val)
            old_to_new[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return old_to_new[node]
        
        return dfs(node) if node else None