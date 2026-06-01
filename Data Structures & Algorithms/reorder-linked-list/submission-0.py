# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reverse the second half

        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #merge

        mergeCurr = dummy = ListNode()

        while prev and head != prev:
            mergeCurr.next = head
            head = head.next
            mergeCurr.next.next = prev
            mergeCurr = prev
            prev = prev.next
        
        mergeCurr.next = prev




        
