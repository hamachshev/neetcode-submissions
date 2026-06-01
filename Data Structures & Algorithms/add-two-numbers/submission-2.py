# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        sum = 0
        place = 1
        while curr1:
            sum += curr1.val * place
            place *= 10
            curr1 = curr1.next
        
        place = 1
        while curr2:
            sum += curr2.val * place
            place *= 10
            curr2 = curr2.next
        
        dummy= head  = ListNode(0)
        if sum == 0: return dummy
        while sum > 0:
            head.next = ListNode(sum%10)
            head = head.next
            sum //= 10
        return dummy.next
        
