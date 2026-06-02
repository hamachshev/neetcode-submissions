# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_peel(root, subroot):
            if not subroot and not root: return True
            if not root or not subroot: return False
            if root.val != subroot.val:
                return False
            if root.val == subroot.val:
                if check_peel(root.right,subroot.right ) and check_peel(root.left, subroot.left):
                    return True
        
            
        def check(root, subroot):
            if not subroot and not root: return True
            if not root or not subroot: return False

            if root.val == subroot.val:
                if check_peel(root.right,subroot.right ) and check_peel(root.left, subroot.left):
                    return True
        
            return check(root.right, subroot) or check(root.left, subroot)
        return check(root, subRoot)