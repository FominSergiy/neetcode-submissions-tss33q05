# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = self.merge_lists(lists[i - 1], lists[i])
        
        return lists[-1]

    def merge_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        # always pick the smallest
        while l1 and l2:
            if l1.val >= l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        
        return dummy.next
        

        