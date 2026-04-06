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
        node_map = {}
        curr = head
        while curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node
            curr = curr.next
        
        new_head = node_map[head]
        dummy = Node(0,next=new_head)

        # iterate 1 more time and create pointers if exist
        curr = head
        while curr:
            new_curr = node_map[curr]

            if curr.next:
                old_nn = curr.next
                new_nn = node_map[old_nn]
                new_curr.next = new_nn
            
            if curr.random:
                old_random = curr.random
                new_random = node_map[old_random]
                new_curr.random = new_random

            curr = curr.next

        return dummy.next
