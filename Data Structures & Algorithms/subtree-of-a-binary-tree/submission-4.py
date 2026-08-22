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
        right = IsSame(p.right, q.right)
    
    return left and right

def Search(p,q):
    if not p:
        return False
    else:
        if p.val == q.val:
            if IsSame(p, q):
                return True
        left = Search(p.left,q)
        right = Search(p.right,q)
        
    return left or right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return Search(root, subRoot)
        