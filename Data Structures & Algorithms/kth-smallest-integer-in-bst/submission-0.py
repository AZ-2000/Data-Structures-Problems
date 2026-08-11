# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(node, res):
    if not node:
        return
    else:
        inorder(node.left,res)
        res.append(node.val)
        inorder(node.right,res)
    return res
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        res = inorder(root, res)
        print(res)
        i = 0
        while i < len(res):
            if i == k-1:
                return res[i]
            i += 1

