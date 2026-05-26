# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def helper(self, node):
        if not node:
            return 0
        left_path = self.helper(node.left)
        right_path = self.helper(node.right)
        self.diameter = max(self.diameter, left_path + right_path)

        return 1 + max(left_path, right_path)

    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.diameter
             