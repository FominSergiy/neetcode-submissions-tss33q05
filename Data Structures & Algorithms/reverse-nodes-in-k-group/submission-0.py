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
        counter = 0
        cur = head

        new_head = None

        segment_to_be_tail = cur
        prev_segment_tail = None

        while cur:
            counter += 1
            # print('\n')
            # print(counter)
            if counter % k == 0: # segment found
                
                # 1. save next node and cut the segment
                next_node = cur.next
                cur.next = None

                # 2. reverse this segment
                top_of_reversed = self.reverse_list(segment_to_be_tail)
                # self._print_nodes(prev_segment_tail)
                # self._print_nodes(top_of_reversed)

                # 3. set reversed head once
                if not new_head:
                    new_head = top_of_reversed
                
                # 4. link previous tail to this head
                if prev_segment_tail:
                    prev_segment_tail.next = top_of_reversed
                
                # 5. set new tail for this segment
                prev_segment_tail = segment_to_be_tail
                
                # 6. update pointer to next segment from prev head (now tail)
                segment_to_be_tail.next = next_node

                # 7. set head for new segment
                segment_to_be_tail = next_node

                # 8. update cur pointer
                cur = segment_to_be_tail
            else:
                cur = cur.next

        # linked list did not have at least k nodes
        if not new_head:
            return head
        return new_head


    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            next_node = cur.next
            cur.next = prev

            prev = cur
            cur = next_node
        
        return prev


        