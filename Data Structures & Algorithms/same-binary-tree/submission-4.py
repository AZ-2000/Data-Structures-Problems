# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def IsSame(p,q, flag):
    if not p and not q:
        return
    else:
        if not p or not q or p.val != q.val:
            flag[0] = False
        else:
            IsSame(p.left, q.left, flag)
            IsSame(p.right, q.right, flag)
    
    
    

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = [True]
        IsSame(p,q, flag)
        return flag[0]

       
        