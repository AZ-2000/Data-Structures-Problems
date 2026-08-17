# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValid(node, subtreenode):
    if not node and not subtreenode:
        return True
    else:
        if not node or not subtreenode or node.val!=subtreenode.val:
            return False
        left =  isValid(node.left,subtreenode.left)
        right = isValid(node.right, subtreenode.right)
        return left and right

def search(node, subtreenode):
    if not node:
        return False
    else:
        if node.val == subtreenode.val:
            if isValid(node,subtreenode):
                return True

        left = search(node.left, subtreenode)
        right = search(node.right, subtreenode)
        return left or right
    
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return search(root, subRoot)