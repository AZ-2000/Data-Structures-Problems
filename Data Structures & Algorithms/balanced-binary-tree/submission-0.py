# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node,res):
        if not node:
            return 0
        else:
            left_height = self.helper(node.left,res)
            right_height = self.helper(node.right,res)
            res.append(abs(left_height-right_height))
            return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.helper(root, res)
        
        for item in res:
            if item not in [-1,0,1]:
                return False
        return True