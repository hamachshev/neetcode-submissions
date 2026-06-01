# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        _set = set()
        _set.add(head)
        while head:
            if head.next in _set:
                return True
            _set.add(head.next)
            head = head.next
        return False