# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we are looking for a node that is either = to one of the p/q or between
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        if root.val == p.val or root.val == q.val or (root.val < p.val and root.val > q.val) or (root.val > p.val and root.val < q.val):
            return root
        return self.lowestCommonAncestor(root.right, p,  q) or self.lowestCommonAncestor(root.left, p, q)
        