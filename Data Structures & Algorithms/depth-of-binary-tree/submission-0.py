# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def recurse(root: Optional[TreeNode], dep: int):
            nonlocal depth
            if not root:
                return
            if not root.right and not root.left:
                depth = max(depth, dep)
            recurse(root.left, dep + 1)
            recurse(root.right, dep + 1)
        recurse(root, 1)
        return depth
            