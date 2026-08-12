# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(node, maxval, counter=0):
    if not node:
        return 0
    else:
        if node.val >= maxval:
            counter = 1
            maxval = node.val
        counter += helper(node.left, maxval)
        counter += helper(node.right, maxval)
    return counter
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return helper(root, float('-inf'), 0)
        