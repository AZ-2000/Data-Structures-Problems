# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(root, max_val):
    if not root:
        return 0
    else:
        left_path = helper(root.left, max_val)
        right_path = helper(root.right, max_val)
        left = max(0, left_path)
        right = max(0, right_path)
        max_val[0] = max(max_val[0], right + left+root.val)
    
    return root.val + max(left, right)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = [float("-infinity")]
        helper(root, max_val)
        return max_val[0]
               
        

        