# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recurse(root: Optional[TreeNode])-> tuple[int, int]:
            if not root:
                return 0, 0
            left, dep_right  = recurse(root.left)
            right, dep_left = recurse(root.right) 
            
            if root.right:
                right +=1
            if root.left:
                left+=1
            dep = max(dep_right, dep_left, (right + left)) 
  
            return max(right, left), dep
        
        return recurse(root)[1]