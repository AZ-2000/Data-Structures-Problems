# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(node,bigger,smaller,LCA):

    if node.val >= smaller.val and node.val <= bigger.val:
        LCA = node
        return LCA
    else:
        if node.val > smaller.val and node.val > bigger.val:
            print(node.val, smaller.val, bigger.val)
            node = helper(node.left, bigger, smaller, LCA)
        elif node.val < smaller.val and node.val < bigger.val:
            print(node.val, smaller.val, bigger.val, LCA)
            node = helper(node.right, bigger, smaller, LCA)
    return node
    
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = None
        if p.val >= q.val:
            bigger = p
            smaller = q
        else:
            bigger = q
            smaller = p
        LCA = helper(root, bigger, smaller, LCA)
        return LCA