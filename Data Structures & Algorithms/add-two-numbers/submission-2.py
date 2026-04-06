# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        # both lists of same size
        carry = 0
        while l1 and l2:
            cur_sum = l1.val + l2.val + carry
            carry = 0

            # either split on carry or move carry forward
            if cur_sum > 9:
                digit = cur_sum % 10
                new_node = ListNode(digit)
                carry = cur_sum // 10
                curr.next = new_node
            else:
                new_node = ListNode(cur_sum)
                curr.next = new_node

            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        remain = l1 or l2

        if remain:
            if not carry:
                curr.next = remain
            else:

                while remain:
                    cur_sum = remain.val + carry
                    carry = 0

                    if cur_sum > 9:
                        digit = cur_sum % 10
                        new_node = ListNode(digit)
                        carry = cur_sum // 10
                        curr.next = new_node
                    else:
                        new_node = ListNode(cur_sum)
                        curr.next = new_node
                    
                    remain = remain.next
                    curr = curr.next
        
        if carry:
            curr.next = ListNode(carry)

        
        return dummy.next


        