# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(node,res):
    if not node:
        res.append(None)
    else:
        res.append(node.val)
        left = helper(node.left,res)
        right = helper(node.right,res)
    return res

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = []
        res2 = []
        res = helper(p, res)
        res2 = helper(q,res2)

        if len(res)!= len(res2):
            return False
        else:
            l = 0
            while l < len(res):
                if res[l] != res2[l]:
                    return False
                l += 1
            return True
 
         

        