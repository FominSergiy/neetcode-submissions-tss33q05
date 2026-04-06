"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
    
        # create copy of nodes and store in map
        node_map = { None: None }
        curr = head
        while curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node
            curr = curr.next
        
        # iterate 1 more time and create pointers if exist
        curr = head
        while curr:
            new_curr = node_map[curr]
            new_curr.next = node_map[curr.next]
            new_curr.random = node_map[curr.random]
            curr = curr.next

        return node_map[head]
