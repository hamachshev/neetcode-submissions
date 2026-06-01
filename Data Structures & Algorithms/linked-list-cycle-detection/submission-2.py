# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        _set = set()
        while head:
            if head in _set:
                return True
            _set.add(head)
            head = head.next
        return False