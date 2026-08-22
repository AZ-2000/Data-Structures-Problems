# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def postorder(node,res):
    if not node:
        return
    else:
        postorder(node.left,res)
        postorder(node.right,res)
        res.append(node.val)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        postorder(root,res)
        return res