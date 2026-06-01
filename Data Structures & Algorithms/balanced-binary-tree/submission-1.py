# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def height(root: Optional[TreeNode]):
            nonlocal balanced

            if not root:
                return 0
            
            right = height(root.right)
            left = height(root.left)
            print(right, left)

            balanced = False if abs(right - left) > 1 else balanced
            return max(left, right) + 1  

        height(root)
        return balanced



