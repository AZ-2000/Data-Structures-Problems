# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(node):
    global diameter
    if not node:
        return 0
    else:
        left_path =  helper(node.left)
        right_path = helper(node.right)
        diameter = max(diameter, left_path + right_path)
        return 1 + max(left_path, right_path)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global diameter
        diameter = 0
        helper(root)
        return diameter
        