# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def helper(self, node, maxdiam):
        if not node:
            return 0
        else:
            left_path = self.helper(node.left, maxdiam)
            right_path = self.helper(node.right, maxdiam)
            diameter = left_path + right_path
            self.diameter = max(self.diameter, diameter)

        return 1 + max(left_path, right_path)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0)
        return self.diameter
             