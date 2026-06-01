# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurse(root: Optional[TreeNode], dep: int):
            if not root:
                return dep
            return max(recurse(root.left, dep + 1),
            recurse(root.right, dep + 1))
        return recurse(root, 0)
        
            