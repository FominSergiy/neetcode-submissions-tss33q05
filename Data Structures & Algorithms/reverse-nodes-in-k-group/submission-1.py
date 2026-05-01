# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _print_nodes(self, node: Optional[ListNode]):
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        print(f"node vals: {vals}")
        return

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def recurse(node: Optional[ListNode]) -> Optional[ListNode]:
            cur = node
            group = 0
            
            # ends with cur at k + 1
            while cur and group < k:
                cur = cur.next
                group += 1
            
            if group == k:
                cur = recurse(cur) # cur is k + 1

                # a list reversal but using cur as prev and decrementing group counter
                while group > 0:
                    tmp = node.next
                    node.next = cur
                    cur = node
                    node = tmp
                    group -= 1
                node = cur
        
            return node
        
        return recurse(head)



        