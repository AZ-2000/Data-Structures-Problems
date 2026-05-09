# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangesum(self, node, low, high):
        if node is None:
            return 0
        if node.val >= low and node.val <= high:
            return node.val + (self.rangesum(node.left,low,high)) + self.rangesum(node.right, low, high)
        else:
            return self.rangesum(node.left,low,high) or self.rangesum(node.right, low, high)


    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rangesum = self.rangesum(root, low, high)
        return rangesum