# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def del_leaf(node, target):
    if not node:
        return
    else:
        if (not node.left) and (not node.right) and (node.val == target):
            node = None
            return 
        node.left = del_leaf(node.left, target)
        node.right = del_leaf(node.right, target)
        if (not node.left) and (not node.right) and (node.val == target):
            node = None
            return 
        return node

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        del_leaf(root, target)
        if root.val == target:
            root = None
        
        return root
        