# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(node,max_val):
    if not node:
        return 0
    else:

        left_path = dfs(node.left, max_val)
        right_path = dfs(node.right, max_val)

        left = max(0, left_path)
        right = max(0, right_path)

        max_val[0] = max(max_val[0], left + right + node.val)
        
        
        return node.val + max(left, right)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = [float('-infinity')]
        dfs(root, max_val)
        return max_val[0]        
        

        