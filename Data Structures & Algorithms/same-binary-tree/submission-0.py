# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recurse(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p or not q:
                return True if not p and not q else False
            if p.val != q.val:
                return False
            return recurse(p.right, q.right) and recurse(p.left, q.left)
        return recurse(p,q)