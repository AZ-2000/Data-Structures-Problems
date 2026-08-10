# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(node):
    if not node:
        return 0
    else:
        left = helper(node.left)
        right = helper(node.right)
        return 1 + max(left, right)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return helper(root)
        