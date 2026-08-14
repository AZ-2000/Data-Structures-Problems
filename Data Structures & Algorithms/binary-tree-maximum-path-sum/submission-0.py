# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(node, maxval):
    if node is None:
        return 0
    else:
        left_path = max(0, helper(node.left,maxval))
        right_path = max(0, helper(node.right, maxval))

        maxval[0] = max(maxval[0], left_path + right_path+node.val)
    
    return node.val + max(left_path, right_path)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxval = [float('-infinity')]

        helper(root, maxval)
        return maxval[0]

        