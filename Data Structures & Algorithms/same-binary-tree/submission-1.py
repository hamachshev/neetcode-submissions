# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q_queue = deque()
        p_queue = deque()

        q_queue.append(q)
        p_queue.append(p)

        while q_queue and p_queue:
            p = p_queue.popleft()
            q = q_queue.popleft()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            p_queue.append(p.right)
            p_queue.append(p.left)
            q_queue.append(q.right)
            q_queue.append(q.left)
        return len(q_queue) == len(p_queue)
            