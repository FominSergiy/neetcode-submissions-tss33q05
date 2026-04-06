# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            
            # set pointer of this elem to prev
            curr.next = prev
            
            #reset the prev to this node for future
            prev = curr

            # move in while loop to next one
            curr = next_node
        
        return prev

        # next-node = 1
        # prev = none
        # dummy = 0
        # reset prev
        #
        #
        #
        