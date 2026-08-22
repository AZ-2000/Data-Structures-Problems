# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(node,res):
    if not node:
        return
    else:
        inorder(node.left,res)
        res.append(node.val)
        inorder(node.right,res)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        inorder(root,res)
        return res
        