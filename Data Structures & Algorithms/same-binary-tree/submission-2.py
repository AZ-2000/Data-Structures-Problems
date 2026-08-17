# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def IsSame(p,q):
    if not p and not q:
        return True
    else:
        if not p or not q or p.val != q.val:
            return False
        
        left = IsSame(p.left, q.left)
        right = IsSame(p.right,q.right)

        return left and right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return IsSame(p,q)
        