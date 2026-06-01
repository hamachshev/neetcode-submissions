# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        carry = 0
        while True:
            sum = (curr1.val + curr2.val + carry)
            carry =  sum // 10 
            curr1.val = sum % 10

            if not curr1.next or not curr2.next: break

            curr1, curr2 = curr1.next, curr2.next
        
        if curr2.next:
            curr1.next = curr2.next
        if curr1.next:
            curr1 = curr1.next
        elif carry > 0:
            curr1.next = ListNode(0)
            curr1 = curr1.next
        #carry
        while carry > 0:
            sum = (curr1.val + carry)
            carry = sum // 10
            curr1.val = sum % 10
            if curr1.next:
                curr1 = curr1.next
            elif carry > 0:
                curr1.next = ListNode(0)
                curr1 = curr1.next
        
        return l1

       
