# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        flag = False

        def check(root, subroot):
            nonlocal flag

            if not subroot and not root: return True
            if not root or not subroot: return False

            if flag and root.val != subroot.val:
                return False

            if root.val == subroot.val:
                flag = True
                if check(root.right,subroot.right ) and check(root.left, subroot.left):
                    return True
            flag = False
            return check(root.right, subroot) or check(root.left, subroot)
        return check(root, subRoot)