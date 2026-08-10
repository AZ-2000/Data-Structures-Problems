# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(node):
    if not node:
        return
    else:
        left = helper(node.left)
        right = helper(node.right)
        node.left = right
        node.right = left

        return node

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return helper(root)

