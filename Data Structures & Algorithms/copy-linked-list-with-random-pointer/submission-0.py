"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        _dict= {}
        newHead= curr = Node(0)
        while head:
            if head in _dict:
                curr.next = _dict[head]
                curr = curr.next
            else:
                curr.next = Node(head.val)
                curr = curr.next
                _dict[head] = curr

            if head.random and head.random in _dict:
                curr.random = _dict[head.random]
            elif head.random:
                curr.random = Node(head.random.val)
                _dict[head.random] = curr.random
            head = head.next
        return newHead.next
