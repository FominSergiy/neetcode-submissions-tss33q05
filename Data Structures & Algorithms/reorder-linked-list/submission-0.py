# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        1 find middle of the list
        2 reverse the 2nd half of the list
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split list in two
        right_side = slow.next
        slow.next = None

        # reverse 2nd half
        prev = None
        curr = right_side
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        right_side = prev
        left_side = head

        # create final reordered list
        while left_side and right_side:
            tmp_l, tmp_r = left_side.next, right_side.next
            left_side.next = right_side
            right_side.next = tmp_l
            left_side, right_side = tmp_l, tmp_r
        
        return