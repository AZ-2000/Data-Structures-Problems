# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def depthcalc(node):
    if not node:
        return 0
    else:
        left_path = depthcalc(node.left)
        right_path = depthcalc(node.right)

    return 1 + max(left_path, right_path)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return depthcalc(root)
        