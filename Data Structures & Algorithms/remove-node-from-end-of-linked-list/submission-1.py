# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        def rec(head1):
            
            if not head1: 
                return 0

            count  = 1 + rec(head1.next)
            if count == n + 1:
                head1.next= head1.next.next
            return count
        
        dummy = ListNode()
        dummy.next =head
        rec(dummy)
        return dummy.next
