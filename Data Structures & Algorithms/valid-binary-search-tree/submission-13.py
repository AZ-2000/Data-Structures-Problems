# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(node,left, right):
    if not node:
        return True
    else:
        if node.val <= left or node.val >= right:
            return False
        left_path = helper(node.left, left, node.val)
        right_path = helper(node.right, node.val, right)

    return left_path and right_path

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return helper(root, float("-infinity"), float("infinity"))
        