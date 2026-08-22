# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorder(node, res):
    if not node:
        return
    else:
        res.append(node.val)
        preorder(node.left,res)
        preorder(node.right, res)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        preorder(root, res)
        return res