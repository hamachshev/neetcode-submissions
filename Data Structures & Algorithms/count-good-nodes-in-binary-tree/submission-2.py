# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
  
        def recurse(root, greatest):
            if not root: return 0
            count = 0
            if root and root.val >= greatest:
                count += 1
                greatest = root.val

            if root.right: count += recurse(root.right, greatest)
            if root.left: count += recurse(root.left, greatest)
            return count
        return recurse(root, root.val)


