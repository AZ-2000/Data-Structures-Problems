# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(node,maxval,res):
    if not node:
        return 0
    else:
        if node.val >= maxval:
            res.append(node.val)
        maxval = max(maxval,node.val)
        left = helper(node.left,maxval,res)
        right = helper(node.right,maxval,res)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxval = float("-infinity")
        res = []
        helper(root, maxval, res)
        # print(res)
        return len(res)
        